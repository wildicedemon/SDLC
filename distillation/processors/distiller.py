"""Research distillation orchestrator - coordinates the complete distillation pipeline."""

import asyncio
import gc
import logging
import psutil
import time
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, List, Optional, Any, Union
from concurrent.futures import ThreadPoolExecutor, as_completed

from ..models import (
    KnowledgeAtom,
    ProductSpec,
    SystemConfig,
    DistillationConfig,
    ResearchFile,
)
from ..models.base import EvidenceStrength, ProductCategory
from .ingestion import ResearchIngestor
from .extraction import AtomExtractor
from .domain_mapper import DomainMapper
from .phase_assigner import PhaseAssigner
from .product_assembler import ProductAssembler
from .monitor import PipelineMonitor, MonitoringContext


@dataclass
class PipelineMetrics:
    """Metrics collected during pipeline execution."""

    start_time: float
    end_time: Optional[float] = None
    files_processed: int = 0
    atoms_extracted: int = 0
    products_generated: int = 0
    errors: List[str] = None
    memory_peak_mb: float = 0.0
    memory_current_mb: float = 0.0
    processing_time_seconds: float = 0.0
    cpu_percent: float = 0.0

    def __post_init__(self):
        if self.errors is None:
            self.errors = []

    @property
    def total_time(self) -> float:
        """Total execution time in seconds."""
        if self.end_time is None:
            return time.time() - self.start_time
        return self.end_time - self.start_time

    def update_memory_stats(self) -> None:
        """Update current memory statistics."""
        try:
            process = psutil.Process()
            memory_info = process.memory_info()
            self.memory_current_mb = memory_info.rss / 1024 / 1024  # Convert to MB
            self.memory_peak_mb = max(self.memory_peak_mb, self.memory_current_mb)
            self.cpu_percent = process.cpu_percent()
        except Exception:
            # If psutil fails, continue without memory monitoring
            pass

    def complete(self) -> None:
        """Mark pipeline as completed."""
        self.end_time = time.time()
        self.processing_time_seconds = self.total_time
        self.update_memory_stats()


class ResearchDistiller:
    """Orchestrator for the complete research distillation pipeline.

    Coordinates all processing stages:
    1. Research ingestion (parallel/async)
    2. Knowledge atom extraction
    3. Domain and phase mapping
    4. Product assembly and validation
    """

    def __init__(self, config: SystemConfig):
        """Initialize the distiller with configuration."""
        self.config = config
        self.logger = logging.getLogger(__name__)

        # Initialize processors
        self.ingestor = ResearchIngestor()
        self.extractor = AtomExtractor(config.extraction)
        self.domain_mapper = DomainMapper()
        self.phase_assigner = PhaseAssigner()
        self.product_assembler = ProductAssembler(config.templates)

        # Pipeline state
        self.research_files: List[ResearchFile] = []
        self.knowledge_atoms: List[KnowledgeAtom] = []
        self.product_specs: List[ProductSpec] = []
        self.metrics = PipelineMetrics(start_time=time.time())

    async def distill_corpus(self, input_dir: Path) -> Dict[str, Any]:
        """Run the complete distillation pipeline on a research corpus.

        Args:
            input_dir: Directory containing research files

        Returns:
            Dictionary with pipeline results and metrics
        """
        try:
            self.logger.info(f"Starting distillation pipeline on {input_dir}")
            self.metrics.update_memory_stats()

            # Validate input
            if not input_dir.exists():
                raise ValueError(f"Input directory does not exist: {input_dir}")
            if not input_dir.is_dir():
                raise ValueError(f"Input path is not a directory: {input_dir}")

            # Phase 1: Ingest research files (async)
            await self._ingest_research_files(input_dir)
            self.metrics.update_memory_stats()
            self._check_memory_limits()

            # Phase 2: Extract knowledge atoms
            await self._extract_knowledge_atoms()
            self.metrics.update_memory_stats()
            self._check_memory_limits()

            # Phase 3: Map domains and phases
            self._map_domains_and_phases()
            self.metrics.update_memory_stats()

            # Phase 4: Assemble products
            self._assemble_products()
            self.metrics.update_memory_stats()

            # Phase 5: Validate and finalize
            self._validate_pipeline()
            self.metrics.update_memory_stats()

            # Force garbage collection before completion
            gc.collect()
            self.metrics.complete()

            return {
                "success": True,
                "metrics": self._get_metrics_dict(),
                "atoms": [atom.to_dict() for atom in self.knowledge_atoms],
                "products": [spec.to_yaml_dict() for spec in self.product_specs],
                "files_processed": len(self.research_files),
            }

        except Exception as e:
            self.logger.error(f"Pipeline failed: {e}")
            self.metrics.errors.append(str(e))

            # Force garbage collection on error
            gc.collect()
            self.metrics.complete()

            # Attempt partial recovery - return what we have
            return {
                "success": False,
                "error": str(e),
                "metrics": self._get_metrics_dict(),
                "atoms": [atom.to_dict() for atom in self.knowledge_atoms],
                "products": [spec.to_yaml_dict() for spec in self.product_specs],
                "partial_results": True,
            }

    async def _ingest_research_files(self, input_dir: Path) -> None:
        """Phase 1: Ingest all research files asynchronously."""
        self.logger.info("Phase 1: Ingesting research files")

        # Discover all files
        research_files = self._discover_research_files(input_dir)
        self.logger.info(f"Found {len(research_files)} research files")

        # Process files concurrently
        if self.config.distillation.enable_async:
            self.research_files = await self._ingest_files_async(research_files)
        else:
            self.research_files = self._ingest_files_sync(research_files)

        self.metrics.files_processed = len(self.research_files)
        self.logger.info(f"Successfully ingested {len(self.research_files)} files")

    def _discover_research_files(self, input_dir: Path) -> List[Path]:
        """Discover all supported research files in the input directory."""
        supported_extensions = set(self.config.distillation.supported_formats)
        research_files = []

        for file_path in input_dir.rglob("*"):
            if file_path.is_file():
                if file_path.stat().st_size > self.config.distillation.max_file_size:
                    self.logger.warning(f"Skipping large file: {file_path} ({file_path.stat().st_size} bytes)")
                    continue

                if file_path.suffix.lower().lstrip('.') in supported_extensions:
                    research_files.append(file_path)

        return research_files

    async def _ingest_files_async(self, file_paths: List[Path]) -> List[ResearchFile]:
        """Ingest files asynchronously with concurrency control."""
        semaphore = asyncio.Semaphore(self.config.distillation.max_concurrent_files)
        ingested_files = []

        async def ingest_single_file(file_path: Path) -> Optional[ResearchFile]:
            async with semaphore:
                try:
                    # Add timeout to prevent hanging
                    result = await asyncio.wait_for(
                        asyncio.get_event_loop().run_in_executor(
                            None, self.ingestor.ingest_file, file_path
                        ),
                        timeout=30.0  # 30 second timeout per file
                    )
                    return result
                except asyncio.TimeoutError:
                    error_msg = f"Ingestion timeout for {file_path}"
                    self.logger.error(error_msg)
                    self.metrics.errors.append(error_msg)
                    return None
                except Exception as e:
                    error_msg = f"Failed to ingest {file_path}: {e}"
                    self.logger.error(error_msg)
                    self.metrics.errors.append(error_msg)
                    return None

        # Process files in batches to avoid overwhelming the system
        batch_size = self.config.distillation.max_concurrent_files * 2
        for i in range(0, len(file_paths), batch_size):
            batch = file_paths[i:i + batch_size]
            tasks = [ingest_single_file(path) for path in batch]
            results = await asyncio.gather(*tasks, return_exceptions=True)

            for result in results:
                if isinstance(result, ResearchFile):
                    ingested_files.append(result)
                elif isinstance(result, Exception):
                    error_msg = f"Async ingestion error: {result}"
                    self.logger.error(error_msg)
                    self.metrics.errors.append(error_msg)

            # Brief pause between batches to prevent resource exhaustion
            if i + batch_size < len(file_paths):
                await asyncio.sleep(0.1)

        return ingested_files

    def _ingest_files_sync(self, file_paths: List[Path]) -> List[ResearchFile]:
        """Ingest files synchronously with thread pool for I/O bound operations."""
        ingested_files = []

        with ThreadPoolExecutor(max_workers=self.config.distillation.max_concurrent_files) as executor:
            future_to_path = {
                executor.submit(self.ingestor.ingest_file, path): path
                for path in file_paths
            }

            for future in as_completed(future_to_path):
                path = future_to_path[future]
                try:
                    research_file = future.result()
                    ingested_files.append(research_file)
                except Exception as e:
                    self.logger.error(f"Failed to ingest {path}: {e}")
                    self.metrics.errors.append(f"Ingestion failed for {path}: {e}")

        return ingested_files

    async def _extract_knowledge_atoms(self) -> None:
        """Phase 2: Extract knowledge atoms from research files."""
        self.logger.info("Phase 2: Extracting knowledge atoms")

        # Extract atoms from all files with error recovery
        all_atoms = []
        extraction_errors = 0
        max_errors = len(self.research_files) // 4  # Allow up to 25% failure rate

        for research_file in self.research_files:
            try:
                atoms = self.extractor.extract_atoms(research_file)
                all_atoms.extend(atoms)
            except Exception as e:
                extraction_errors += 1
                error_msg = f"Failed to extract atoms from {research_file.file_path}: {e}"
                self.logger.error(error_msg)
                self.metrics.errors.append(error_msg)

                # If too many files fail, abort extraction phase
                if extraction_errors > max_errors:
                    raise RuntimeError(f"Too many extraction failures ({extraction_errors}/{len(self.research_files)}). Aborting pipeline.")

        # Check if we have minimum viable atoms
        if len(all_atoms) == 0:
            raise RuntimeError("No knowledge atoms extracted from any files. Pipeline cannot continue.")

        # Deduplicate atoms
        try:
            self.knowledge_atoms = self._deduplicate_atoms(all_atoms)
        except Exception as e:
            self.logger.error(f"Failed to deduplicate atoms: {e}")
            # Continue with non-deduplicated atoms as fallback
            self.knowledge_atoms = all_atoms
            self.metrics.errors.append(f"Deduplication failed, using raw atoms: {e}")

        self.metrics.atoms_extracted = len(self.knowledge_atoms)

        # Warn if extraction success rate is low
        success_rate = (len(self.research_files) - extraction_errors) / len(self.research_files)
        if success_rate < 0.8:  # Less than 80% success
            self.logger.warning(f"Low extraction success rate: {success_rate:.1%}")

        self.logger.info(f"Extracted {len(self.knowledge_atoms)} unique knowledge atoms from {len(self.research_files) - extraction_errors}/{len(self.research_files)} files")

    def _deduplicate_atoms(self, atoms: List[KnowledgeAtom]) -> List[KnowledgeAtom]:
        """Deduplicate atoms based on content similarity with memory optimization."""
        if not atoms:
            return []

        # For large datasets, use streaming deduplication to save memory
        if len(atoms) > 1000:
            return self._deduplicate_atoms_streaming(atoms)
        else:
            return self._deduplicate_atoms_in_memory(atoms)

    def _deduplicate_atoms_in_memory(self, atoms: List[KnowledgeAtom]) -> List[KnowledgeAtom]:
        """Simple in-memory deduplication for smaller datasets."""
        seen_content = set()
        unique_atoms = []

        for atom in atoms:
            # Create a normalized content hash
            content_key = atom.content.strip().lower()[:200]  # Limit content for hash
            content_hash = hash(content_key)

            if content_hash not in seen_content:
                seen_content.add(content_hash)
                unique_atoms.append(atom)

        return unique_atoms

    def _deduplicate_atoms_streaming(self, atoms: List[KnowledgeAtom]) -> List[KnowledgeAtom]:
        """Streaming deduplication for large datasets to save memory."""
        from collections import defaultdict

        # Group by content similarity first (more memory efficient)
        content_groups = defaultdict(list)

        for atom in atoms:
            # Use first 100 chars + type for grouping key
            key = f"{atom.type.value}:{atom.content.strip().lower()[:100]}"
            content_groups[key].append(atom)

        # Select best atom from each group
        unique_atoms = []
        for group in content_groups.values():
            if len(group) == 1:
                unique_atoms.append(group[0])
            else:
                # Prefer atom with strongest evidence
                best_atom = max(group, key=lambda a: self._evidence_strength_score(a))
                unique_atoms.append(best_atom)

        return unique_atoms

    def _evidence_strength_score(self, atom: KnowledgeAtom) -> int:
        """Calculate evidence strength score for atom ranking."""
        score = 0
        if atom.evidence_strength.value == "STRONG":
            score = 3
        elif atom.evidence_strength.value == "MODERATE":
            score = 2
        else:  # WEAK
            score = 1

        # Bonus for multiple sources
        score += len(atom.source) - 1

        return score

    def _map_domains_and_phases(self) -> None:
        """Phase 3: Map atoms to domains and SDLC phases."""
        self.logger.info("Phase 3: Mapping domains and phases")

        for atom in self.knowledge_atoms:
            # Map to domains
            atom.domains = self.domain_mapper.map_to_domains(atom)

            # Map to phases
            atom.sdlc_phases = self.phase_assigner.assign_phases(atom)

        self.logger.info("Completed domain and phase mapping")

    def _assemble_products(self) -> None:
        """Phase 4: Assemble product specifications."""
        self.logger.info("Phase 4: Assembling product specifications")

        # Group atoms by product category
        atoms_by_product = self._group_atoms_by_product()

        # Generate specifications for each product category
        for product_category, atoms in atoms_by_product.items():
            try:
                specs = self.product_assembler.assemble_products(product_category, atoms)
                self.product_specs.extend(specs)
            except Exception as e:
                self.logger.error(f"Failed to assemble {product_category} products: {e}")
                self.metrics.errors.append(f"Product assembly failed for {product_category}: {e}")

        self.metrics.products_generated = len(self.product_specs)
        self.logger.info(f"Generated {len(self.product_specs)} product specifications")

    def _group_atoms_by_product(self) -> Dict[ProductCategory, List[KnowledgeAtom]]:
        """Group knowledge atoms by the product categories they feed."""
        atoms_by_product = {}

        for atom in self.knowledge_atoms:
            for product in atom.products:
                if product not in atoms_by_product:
                    atoms_by_product[product] = []
                atoms_by_product[product].append(atom)

        return atoms_by_product

    def _validate_pipeline(self) -> None:
        """Phase 5: Validate pipeline results and generate gap analysis."""
        self.logger.info("Phase 5: Validating pipeline results")

        # Cross-reference validation
        self._validate_cross_references()

        # Gap analysis
        self._perform_gap_analysis()

        self.logger.info("Pipeline validation completed")

    def _validate_cross_references(self) -> None:
        """Validate that all references between atoms and products are consistent."""
        # Check that all atoms referenced by products exist
        atom_ids = {atom.id for atom in self.knowledge_atoms}

        for spec in self.product_specs:
            for atom_id in spec.knowledge_atoms:
                if atom_id not in atom_ids:
                    self.logger.warning(f"Product {spec.name} references non-existent atom {atom_id}")
                    self.metrics.errors.append(f"Broken reference: {spec.name} -> {atom_id}")

    def _perform_gap_analysis(self) -> None:
        """Analyze gaps in the research coverage."""
        # Count atoms by evidence strength
        evidence_counts = {}
        for atom in self.knowledge_atoms:
            strength = atom.evidence_strength
            evidence_counts[strength] = evidence_counts.get(strength, 0) + 1

        # Identify product categories with weak coverage
        product_coverage = {}
        for spec in self.product_specs:
            if spec.category not in product_coverage:
                product_coverage[spec.category] = []
            product_coverage[spec.category].append(spec.confidence)

        # Log gap analysis
        self.logger.info("Gap Analysis:")
        self.logger.info(f"  Evidence distribution: {evidence_counts}")
        self.logger.info(f"  Products by category: { {k: len(v) for k, v in product_coverage.items()} }")

    def _check_memory_limits(self) -> None:
        """Check if memory usage exceeds safe limits."""
        if self.metrics.memory_current_mb > 100:  # 100MB limit
            self.logger.warning(f"High memory usage: {self.metrics.memory_current_mb:.1f}MB")
            # Force garbage collection
            gc.collect()
            self.metrics.update_memory_stats()

            if self.metrics.memory_current_mb > 150:  # 150MB critical limit
                raise MemoryError(f"Memory usage too high: {self.metrics.memory_current_mb:.1f}MB. Pipeline aborted for safety.")

    def _get_metrics_dict(self) -> Dict[str, Any]:
        """Convert metrics to dictionary format."""
        return {
            "processing_time_seconds": self.metrics.processing_time_seconds,
            "files_processed": self.metrics.files_processed,
            "atoms_extracted": self.metrics.atoms_extracted,
            "products_generated": self.metrics.products_generated,
            "errors_count": len(self.metrics.errors),
            "errors": self.metrics.errors[:10],  # Limit error output
            "memory_peak_mb": self.metrics.memory_peak_mb,
            "memory_final_mb": self.metrics.memory_current_mb,
            "cpu_percent": self.metrics.cpu_percent,
        }

    def save_results(self, output_dir: Path) -> None:
        """Save pipeline results to output directory."""
        import json
        import yaml

        output_dir.mkdir(parents=True, exist_ok=True)

        # Save knowledge atoms
        atoms_file = output_dir / "knowledge_atoms.json"
        with open(atoms_file, 'w', encoding='utf-8') as f:
            json.dump([atom.to_dict() for atom in self.knowledge_atoms], f, indent=2, ensure_ascii=False)

        # Save product specifications
        products_dir = output_dir / "products"
        products_dir.mkdir(exist_ok=True)

        for spec in self.product_specs:
            spec_file = products_dir / f"{spec.category.value}_{spec.name}.yaml"
            with open(spec_file, 'w', encoding='utf-8') as f:
                yaml.dump(spec.to_yaml_dict(), f, default_flow_style=False, sort_keys=False)

        # Save metrics
        metrics_file = output_dir / "pipeline_metrics.json"
        with open(metrics_file, 'w', encoding='utf-8') as f:
            json.dump(self._get_metrics_dict(), f, indent=2, ensure_ascii=False)

        self.logger.info(f"Results saved to {output_dir}")