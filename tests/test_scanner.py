from devvault.scanner import scan_directory


def test_scan_directory_finds_files(tmp_path):
    (tmp_path / "a.py").write_text("print(1)")
    (tmp_path / "b.md").write_text("# notes")
    result = scan_directory(str(tmp_path))
    assert len(result) == 2