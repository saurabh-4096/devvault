from devvault.scanner import scan_directory


def test_scan_directory_finds_files(tmp_path):
    (tmp_path / "a.py").write_text("print(1)")
    (tmp_path / "b.md").write_text("# notes")
    result = scan_directory(str(tmp_path))
    assert len(result) == 2


def test_scan_directory_ignores_venv(tmp_path):
    (tmp_path / "a.py").write_text("print(1)")
    venv_dir = tmp_path / ".venv" / "lib"
    venv_dir.mkdir(parents=True)
    (venv_dir / "junk.py").write_text("ignored")
    result = scan_directory(str(tmp_path))
    assert len(result) == 1
    assert "junk.py" not in result[0]

def test_parse_gitignore(tmp_path):
    """Should parse .gitignore patterns from a directory."""
    from devvault.scanner import parse_gitignore
    gitignore = tmp_path / ".gitignore"
    gitignore.write_text("*.log\nbuild/")
    patterns = parse_gitignore(str(tmp_path))
    assert "*.log" in patterns
    assert "build/" in patterns


def test_should_ignore_pattern(tmp_path):
    """Files matching gitignore patterns should be excluded."""
    (tmp_path / ".gitignore").write_text("*.tmp\n")
    (tmp_path / "data.tmp").write_text("test")
    (tmp_path / "data.txt").write_text("test")
    from devvault.scanner import scan_directory
    files = scan_directory(str(tmp_path))
    assert any("data.txt" in f for f in files)
    assert not any("data.tmp" in f for f in files)
