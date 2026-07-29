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