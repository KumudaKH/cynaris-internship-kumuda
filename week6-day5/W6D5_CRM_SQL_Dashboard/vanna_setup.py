from pathlib import Path
from vanna.ollama import Ollama
from vanna.chromadb import ChromaDB_VectorStore

BASE_DIR = Path(__file__).resolve().parent

class CRMVanna(ChromaDB_VectorStore, Ollama):
    def __init__(self, config=None):
        config = config or {}
        ChromaDB_VectorStore.__init__(self, config=config)
        Ollama.__init__(self, config=config)

def get_vanna():
    vn = CRMVanna(config={"model": "llama3.2", "path": str(BASE_DIR / "chroma_db")})
    vn.connect_to_sqlite(str(BASE_DIR / "crm.db"))
    return vn
