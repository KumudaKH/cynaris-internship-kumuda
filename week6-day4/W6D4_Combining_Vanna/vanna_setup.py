"""Requires installed Vanna legacy (<1), ChromaDB and local Ollama model."""
from pathlib import Path
BASE = Path(__file__).resolve().parent

def get_vanna():
    from vanna.ollama import Ollama
    from vanna.chromadb import ChromaDB_VectorStore
    class LocalVanna(ChromaDB_VectorStore, Ollama):
        def __init__(self, config):
            ChromaDB_VectorStore.__init__(self, config=config)
            Ollama.__init__(self, config=config)
    vn = LocalVanna(config={"model": "llama3.2", "path": str(BASE / "chroma_db")})
    vn.connect_to_sqlite(str(BASE / "company.db"))
    return vn
