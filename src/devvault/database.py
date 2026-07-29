import sqlite3
from pathlib import Path

DB_PATH = Path.home() / ".devvault" / "devvault.db"


def get_connection():
    DB_PATH.parent.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(DB_PATH)
    return conn


def init_db():
    conn = get_connection()
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


def save_files(paths: list[str]):
    conn = get_connection()
    for path in paths:
        extension = Path(path).suffix
        conn.execute(
            "INSERT OR IGNORE INTO files (path, extension) VALUES (?, ?)",
            (path, extension),
        )
    conn.commit()
    conn.close()


def count_files() -> int:
    conn = get_connection()
    cursor = conn.execute("SELECT COUNT(*) FROM files")
    count = cursor.fetchone()[0]
    conn.close()
    return count