import os
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import TextLoader
from langchain_ollama import OllamaEmbeddings
from langchain_community.vectorstores import Chroma

CODE_EXT = [".py", ".js", ".ts", ".sql", ".md", ".txt"]

# load the codebase
def load_codebase(path: str):
    docs = []
    for root, _, files in os.walk(path):
        for f in files:
            if any(f.endswith(ext) for ext in CODE_EXT):
                file_path = os.path.join(root, f)
                print(f"Loading: {file_path}")
                docs.append(TextLoader(file_path, encoding="utf-8").load()[0])
    return docs

# split codebase code files in chunks
def chunk_docs(docs):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=800,
        chunk_overlap=100
    )
    return splitter.split_documents(docs)

# feed the chunks to chromadb
def ingest_to_chroma(repo_path: str, persist_dir: str = "./db/chroma"):
    docs = load_codebase(repo_path)
    chunks = chunk_docs(docs)

    vectordb = Chroma.from_documents(
        chunks,
        embedding=OllamaEmbeddings(model="nomic-embed-text"),
        persist_directory=persist_dir
    )
    vectordb.persist()
    print("Ingestion complete.")

if __name__ == "__main__":
    ingest_to_chroma("../source_code")
