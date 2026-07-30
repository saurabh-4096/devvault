from devvault.database import init_db, save_files, search_files


def test_search_finds_matching_content(tmp_path, monkeypatch):
    fake_db = tmp_path / "test.db"
    monkeypatch.setattr("devvault.database.DB_PATH", fake_db)

    init_db()

    test_file = tmp_path / "notes.md"
    test_file.write_text("This is a note about binary search trees")

    save_files([str(test_file)])

    results = search_files("binary search")
    assert len(results) == 1
    assert "notes.md" in results[0]["path"]


def test_search_returns_empty_for_no_match(tmp_path, monkeypatch):
    fake_db = tmp_path / "test.db"
    monkeypatch.setattr("devvault.database.DB_PATH", fake_db)

    init_db()

    test_file = tmp_path / "notes.md"
    test_file.write_text("Completely unrelated content")

    save_files([str(test_file)])

    results = search_files("quantum physics")
    assert len(results) == 0