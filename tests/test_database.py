from devvault.database import get_connection, save_files, count_files
import sqlite3


def test_save_files_and_count(tmp_path, monkeypatch):
    # Point the database at a temporary file for this test only
    fake_db = tmp_path / "test.db"
    monkeypatch.setattr("devvault.database.DB_PATH", fake_db)

    conn = sqlite3.connect(fake_db)
    conn.execute("""
        CREATE TABLE IF NOT EXISTS files (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            path TEXT NOT NULL UNIQUE,
            extension TEXT,
            indexed_at TEXT DEFAULT CURRENT_TIMESTAMP
        )
    """)
    conn.commit()
    conn.close()

    save_files(["a.py", "b.md"])
    assert count_files() == 2

    # Saving the same files again should NOT create duplicates
    save_files(["a.py", "b.md"])
    assert count_files() == 2