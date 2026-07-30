from fastapi import FastAPI
from devvault.scanner import scan_directory
from devvault.database import init_db, save_files, count_files, search_files

app = FastAPI()
init_db()


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/index")
def index(path: str):
    files = scan_directory(path)
    save_files(files)
    return {"indexed": len(files), "total_in_database": count_files()}


@app.get("/search")
def search(q: str, limit: int = 10):
    results = search_files(q, limit=limit)
    return {"query": q, "results": results}