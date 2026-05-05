from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_qdrant import QdrantVectorStore
from dotenv import load_dotenv
import os

load_dotenv()


QDRANT_URL = os.getenv("QDRANT_URL_END_POINT")
QDRANT_API_KEY = os.getenv("QDRANT_API_KEY")

FILE_PATH = "nodejs_learn.pdf"


# 1. Loading the document
loader = PyPDFLoader(file_path=FILE_PATH)
docs = loader.load()

# print(docs[0])



# 2. Split the docs into smaller chunks
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=400
)

chunks = text_splitter.split_documents(documents=docs)



# 3. Vector embeddings from the chunks
embedding_client = OpenAIEmbeddings(
    model="text-embedding-3-large"
)

# 4. Vector store to store the vector embeddings
vector_store = QdrantVectorStore.from_documents(
    documents=chunks,
    embedding=embedding_client,
    url=QDRANT_URL,
    api_key=QDRANT_API_KEY,
    collection_name="learning_rag"
)


print("Indexing of documents done")




# Retrieval Phase
