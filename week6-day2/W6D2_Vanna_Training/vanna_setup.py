
from pathlib import Path
import uuid

from vanna.ollama import Ollama
from vanna.base import VannaBase
import pandas as pd

BASE_DIR = Path(__file__).resolve().parent

class MyVanna(Ollama):
    def __init__(self, config=None):
        config = config or {}
        VannaBase.__init__(self, config=config)
        Ollama.__init__(self, config=config)
        self.question_sql = []
        self.ddl = []
        self.documentation = []

    def generate_embedding(self, data: str, **kwargs):
        return [float(len(data))]

    def get_similar_question_sql(self, question: str, **kwargs):
        question_words = set(question.lower().split())
        matches = [
            item for item in self.question_sql
            if question_words.intersection(set(item["question"].lower().split()))
        ]
        return matches[:kwargs.get("n_results", 10)]

    def get_related_ddl(self, question: str, **kwargs):
        return list(self.ddl)

    def get_related_documentation(self, question: str, **kwargs):
        return list(self.documentation)

    def add_question_sql(self, question: str, sql: str, **kwargs):
        entry_id = str(uuid.uuid4())
        self.question_sql.append({
            "id": entry_id,
            "question": question,
            "sql": sql,
        })
        return entry_id

    def add_ddl(self, ddl: str, **kwargs):
        self.ddl.append(ddl)
        return str(uuid.uuid4())

    def add_documentation(self, documentation: str, **kwargs):
        self.documentation.append(documentation)
        return str(uuid.uuid4())

    def get_training_data(self, **kwargs):
        rows = [
            {
                "id": item["id"],
                "question": item["question"],
                "content": item["sql"],
                "training_data_type": "sql",
            }
            for item in self.question_sql
        ]
        rows.extend(
            {"id": str(uuid.uuid4()), "content": ddl, "training_data_type": "ddl"}
            for ddl in self.ddl
        )
        rows.extend(
            {
                "id": str(uuid.uuid4()),
                "content": documentation,
                "training_data_type": "documentation",
            }
            for documentation in self.documentation
        )
        return pd.DataFrame(rows)

    def remove_training_data(self, entry_id: str, **kwargs):
        for collection in (self.question_sql,):
            for index, item in enumerate(collection):
                if item["id"] == entry_id:
                    del collection[index]
                    return True
        return False

def get_vanna():
    vn = MyVanna(config={
        "model": "llama3.2",
        "path": str(BASE_DIR / "chroma_db")
    })

    vn.connect_to_sqlite(
        str(BASE_DIR / "company.db")
    )

    return vn
