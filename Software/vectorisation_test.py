from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.docstore.document import Document
from pathlib import Path


# Definiranje početnih vrijednosti

# Putanja da 
path_to_datasets = Path("datasets")
embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-mpnet-base-v2")
splitter = RecursiveCharacterTextSplitter(
    chunk_size=500, 
    chunk_overlap=200, 
    length_function=len)
dataset = []

for file in path_to_datasets.glob("*"):
    text = file.read_text(encoding='utf-8')
    dataset.append(Document(page_content=text, metadata={'source': str(path_to_datasets)}))

split_files = splitter.split_documents(dataset)

database = FAISS.from_documents(split_files, embeddings)

database.save_local("vectorised_dataset")
print("Prerađivanje podataka je završilo!")

 