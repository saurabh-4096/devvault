from pathlib import Path


def scan_directory(root: str) -> list[str]:
    """Recursively scan a directory and return paths of all files found."""
    root_path = Path(root)
    files = []
    for path in root_path.rglob("*"):
        if path.is_file() and ".git" not in path.parts:
            files.append(str(path))
    return files