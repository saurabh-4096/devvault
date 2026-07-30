"""Directory scanner with .gitignore support."""

from pathlib import Path
import fnmatch
import os

IGNORED_DIRS = {".git", ".venv", "__pycache__", "node_modules", ".idea", ".vscode"}


def parse_gitignore(directory: str) -> list[str]:
    """Parse .gitignore patterns from a directory, walking up to root."""
    patterns = []
    current = Path(directory).resolve()
    while True:
        gitignore = current / ".gitignore"
        if gitignore.exists():
            with open(gitignore) as f:
                for line in f:
                    line = line.strip()
                    if line and not line.startswith("#"):
                        patterns.append(line)
        if current.parent == current:
            break
        current = current.parent
    return patterns


def _matches_gitignore(path: Path, patterns: list[str]) -> bool:
    """Check if a path matches any gitignore-style pattern."""
    rel = str(path)
    for pattern in patterns:
        if pattern.startswith("!"):
            if fnmatch.fnmatch(rel, pattern[1:]) or fnmatch.fnmatch(path.name, pattern[1:]):
                return False
        elif fnmatch.fnmatch(rel, pattern) or fnmatch.fnmatch(path.name, pattern):
            return True
    return False


def scan_directory(root: str) -> list[str]:
    """Recursively scan a directory, respecting .gitignore files."""
    root_path = Path(root)
    patterns = parse_gitignore(root)
    files = []
    for path in root_path.rglob("*"):
        if path.is_file():
            if any(part in IGNORED_DIRS for part in path.parts):
                continue
            if patterns and _matches_gitignore(path, patterns):
                continue
            files.append(str(path))
    return files
