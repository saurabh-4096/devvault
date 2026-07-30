import sqlite3
from pathlib import Path

DB_PATH = Path.home() / ".devvault" / "devvault.db"

# File extensions we'll actually try to read as text
TEXT_EXTENSIONS = {".py", ".md", ".txt", ".js", ".java", ".json", ".yaml", ".yml", ".ts"}


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
    conn.execute("""
        CREATE VIRTUAL TABLE IF NOT EXISTS files_fts USING fts5(
            path,
            content
        )
    """)
    conn.commit()
    conn.close()


def _read_text_safely(path: str) -> str:
    try:
        if Path(path).suffix in TEXT_EXTENSIONS:
            return Path(path).read_text(errors="ignore")
    except (OSError, UnicodeDecodeError):
        pass
    return ""


def save_files(paths: list[str]):
    conn = get_connection()
    for path in paths:
        extension = Path(path).suffix
        conn.execute(
            "INSERT OR IGNORE INTO files (path, extension) VALUES (?, ?)",
            (path, extension),
        )
        content = _read_text_safely(path)
        if content:
            conn.execute(
                "INSERT INTO files_fts (path, content) VALUES (?, ?)",
                (path, content),
            )
    conn.commit()
    conn.close()


def count_files() -> int:
    conn = get_connection()
    cursor = conn.execute("SELECT COUNT(*) FROM files")
    count = cursor.fetchone()[0]
    conn.close()
    return count


def search_files(query: str, limit: int = 10) -> list[str]:
    conn = get_connection()
    cursor = conn.execute(
        "SELECT path FROM files_fts WHERE files_fts MATCH ? LIMIT ?",
        (query, limit),
    )
    results = [row[0] for row in cursor.fetchall()]
    conn.close()
    return results