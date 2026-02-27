#!/usr/bin/env python3
"""Benchmark script for the distillation pipeline performance."""

import asyncio
import json
import statistics
import time
from pathlib import Path
from typing import Dict, List, Any

from distillation.models import SystemConfig, DistillationConfig
from distillation.processors import ResearchDistiller


class PipelineBenchmark:
    """Benchmark suite for distillation pipeline performance."""

    def __init__(self, input_dir: Path, output_dir: Path):
        """Initialize benchmark with test data."""
        self.input_dir = input_dir
        self.output_dir = output_dir
        self.results = []

    def create_test_configs(self) -> List[SystemConfig]:
        """Create different test configurations for benchmarking."""
        configs = []

        # Base config
        base_config = SystemConfig(
            distillation=DistillationConfig(
                input_dir=self.input_dir,
                output_dir=self.output_dir / "benchmark_base",
                enable_async=False,
                max_concurrent_files=1,
            )
        )
        configs.append(("sync_single", base_config))

        # Async configs with different concurrency levels
        for concurrency in [2, 4, 8]:
            config = SystemConfig(
                distillation=DistillationConfig(
                    input_dir=self.input_dir,
                    output_dir=self.output_dir / f"benchmark_async_{concurrency}",
                    enable_async=True,
                    max_concurrent_files=concurrency,
                )
            )
            configs.append((f"async_{concurrency}", config))

        return configs

    async def run_single_benchmark(self, name: str, config: SystemConfig) -> Dict[str, Any]:
        """Run a single benchmark test."""
        print(f"Running benchmark: {name}")

        start_time = time.time()
        distiller = ResearchDistiller(config)

        try:
            results = await distiller.distill_corpus(config.distillation.input_dir)
            end_time = time.time()

            benchmark_result = {
                "name": name,
                "success": results["success"],
                "total_time": end_time - start_time,
                "metrics": results["metrics"],
                "atoms_count": len(results["atoms"]),
                "products_count": len(results["products"]),
                "files_processed": results["files_processed"],
                "timestamp": time.time(),
            }

            if not results["success"]:
                benchmark_result["error"] = results.get("error", "Unknown error")

            return benchmark_result

        except Exception as e:
            end_time = time.time()
            return {
                "name": name,
                "success": False,
                "total_time": end_time - start_time,
                "error": str(e),
                "timestamp": time.time(),
            }

    async def run_benchmarks(self, iterations: int = 3) -> Dict[str, Any]:
        """Run complete benchmark suite."""
        print("Starting distillation pipeline benchmarks...")

        configs = self.create_test_configs()
        all_results = []

        for name, config in configs:
            config_results = []

            print(f"\nBenchmarking {name} ({iterations} iterations)")

            for i in range(iterations):
                print(f"  Iteration {i + 1}/{iterations}...")
                result = await self.run_single_benchmark(f"{name}_iter_{i+1}", config)
                config_results.append(result)
                all_results.append(result)

                # Brief pause between iterations
                await asyncio.sleep(0.5)

            # Calculate statistics for this config
            successful_runs = [r for r in config_results if r["success"]]
            if successful_runs:
                times = [r["total_time"] for r in successful_runs]
                print(f"  {name} results:")
                print(f"    Success rate: {len(successful_runs)}/{iterations}")
                print(f"    Avg time: {statistics.mean(times):.2f}s")
                print(f"    Min time: {min(times):.2f}s")
                print(f"    Max time: {max(times):.2f}s")
                if len(times) > 1:
                    print(f"    Std dev: {statistics.stdev(times):.2f}s")

        # Generate summary report
        summary = self.generate_summary_report(all_results)
        return summary

    def generate_summary_report(self, results: List[Dict[str, Any]]) -> Dict[str, Any]:
        """Generate comprehensive benchmark summary."""
        successful_results = [r for r in results if r["success"]]

        summary = {
            "benchmark_info": {
                "total_runs": len(results),
                "successful_runs": len(successful_results),
                "failed_runs": len(results) - len(successful_results),
                "success_rate": len(successful_results) / len(results) if results else 0,
                "timestamp": time.time(),
            },
            "performance_summary": {},
            "recommendations": [],
        }

        if successful_results:
            # Group by configuration
            config_groups = {}
            for result in successful_results:
                config_name = result["name"].split("_iter_")[0]
                if config_name not in config_groups:
                    config_groups[config_name] = []
                config_groups[config_name].append(result)

            # Calculate performance stats per config
            for config_name, config_results in config_groups.items():
                times = [r["total_time"] for r in config_results]
                atoms_counts = [r["atoms_count"] for r in config_results]
                products_counts = [r["products_count"] for r in config_results]

                summary["performance_summary"][config_name] = {
                    "runs": len(config_results),
                    "avg_time": statistics.mean(times),
                    "min_time": min(times),
                    "max_time": max(times),
                    "std_time": statistics.stdev(times) if len(times) > 1 else 0,
                    "avg_atoms": statistics.mean(atoms_counts),
                    "avg_products": statistics.mean(products_counts),
                    "throughput_atoms_per_sec": statistics.mean(atoms_counts) / statistics.mean(times),
                }

            # Generate recommendations
            summary["recommendations"] = self.generate_recommendations(summary["performance_summary"])

        return summary

    def generate_recommendations(self, performance_summary: Dict[str, Any]) -> List[str]:
        """Generate performance recommendations based on results."""
        recommendations = []

        if not performance_summary:
            return ["No successful benchmark runs to analyze"]

        # Find best performing configuration
        best_config = min(performance_summary.items(), key=lambda x: x[1]["avg_time"])

        recommendations.append(f"Best performing configuration: {best_config[0]} "
                             f"({best_config[1]['avg_time']:.2f}s average)")

        # Check for async vs sync performance
        sync_times = []
        async_times = []

        for config_name, stats in performance_summary.items():
            if config_name.startswith("sync"):
                sync_times.append(stats["avg_time"])
            elif config_name.startswith("async"):
                async_times.append(stats["avg_time"])

        if sync_times and async_times:
            sync_avg = statistics.mean(sync_times)
            async_avg = statistics.mean(async_times)

            if async_avg < sync_avg:
                improvement = ((sync_avg - async_avg) / sync_avg) * 100
                recommendations.append(f"Async processing improves performance by {improvement:.1f}%")
            else:
                recommendations.append("Sync processing performed better - consider reducing concurrency")

        # Memory and resource recommendations
        for config_name, stats in performance_summary.items():
            if stats.get("memory_peak_mb", 0) > 100:
                recommendations.append(f"High memory usage in {config_name} - consider memory optimization")

        return recommendations

    def save_results(self, summary: Dict[str, Any], output_file: Path):
        """Save benchmark results to file."""
        output_file.parent.mkdir(parents=True, exist_ok=True)

        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(summary, f, indent=2, ensure_ascii=False)

        print(f"\nBenchmark results saved to: {output_file}")

    def print_summary(self, summary: Dict[str, Any]):
        """Print human-readable benchmark summary."""
        print("\n" + "="*60)
        print("DISTILLATION PIPELINE BENCHMARK RESULTS")
        print("="*60)

        info = summary["benchmark_info"]
        print(f"Total runs: {info['total_runs']}")
        print(f"Successful: {info['successful_runs']}")
        print(f"Failed: {info['failed_runs']}")
        print(".1f")

        if summary["performance_summary"]:
            print(f"\n{'Configuration':<20} {'Avg Time':<10} {'Min':<8} {'Max':<8} {'StdDev':<8}")
            print("-" * 60)

            for config_name, stats in summary["performance_summary"].items():
                print(f"{config_name:<20} {stats['avg_time']:<10.2f} "
                      f"{stats['min_time']:<8.2f} {stats['max_time']:<8.2f} "
                      f"{stats['std_time']:<8.2f}")

        if summary["recommendations"]:
            print("\nRECOMMENDATIONS:")
            for rec in summary["recommendations"]:
                print(f"• {rec}")


async def main():
    """Main benchmark execution."""
    import argparse

    parser = argparse.ArgumentParser(description="Benchmark distillation pipeline")
    parser.add_argument(
        "--input-dir", "-i",
        type=Path,
        default=Path("Kimi-Research"),
        help="Input directory containing research files"
    )
    parser.add_argument(
        "--output-dir", "-o",
        type=Path,
        default=Path("benchmark_results"),
        help="Output directory for benchmark results"
    )
    parser.add_argument(
        "--iterations", "-n",
        type=int,
        default=3,
        help="Number of iterations per configuration"
    )

    args = parser.parse_args()

    # Validate input directory
    if not args.input_dir.exists():
        print(f"Error: Input directory {args.input_dir} does not exist")
        return 1

    # Create benchmark runner
    benchmark = PipelineBenchmark(args.input_dir, args.output_dir)

    try:
        # Run benchmarks
        summary = await benchmark.run_benchmarks(args.iterations)

        # Save and display results
        results_file = args.output_dir / "benchmark_summary.json"
        benchmark.save_results(summary, results_file)
        benchmark.print_summary(summary)

        return 0

    except Exception as e:
        print(f"Benchmark failed: {e}")
        return 1


if __name__ == "__main__":
    exit_code = asyncio.run(main())