"""Corpus scanner module for discovering research files."""
from pathlib import Path
from typing import Dict, List


def scan_corpus(root: Path) -> Dict[str, List[Path]]:
    """Scan the corpus directory for research files.
    
    Args:
        root: Root directory to scan
        
    Returns:
        Dictionary mapping file categories to lists of file paths
    """
    result = {
        "perplexity": [],
        "overviews": [],
        "indices": [],
        "kimi_docs": [],
        "kimi_csv": [],
        "root_files": [],
    }
    
    # Implementation would scan for files matching patterns
    # For now, return empty structure
    return result
