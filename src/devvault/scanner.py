from pathlib import Path

IGNORED_DIRS = {".git", ".venv", "__pycache__", "node_modules", ".idea", ".vscode"}


def scan_directory(root: str) -> list[str]:
    """Recursively scan a directory and return paths of all files found,
    skipping common junk/virtual-environment folders."""
    root_path = Path(root)
    files = []
    for path in root_path.rglob("*"):
        if path.is_file() and not any(part in IGNORED_DIRS for part in path.parts):
            files.append(str(path))
    return files