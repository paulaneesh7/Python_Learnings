from dotenv import load_dotenv
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import Chroma



load_dotenv()


# load pdf
docs = PyPDFLoader("cs_sample.pdf").load()


# split into chunks
splitter = RecursiveCharacterTextSplitter(
    chunk_size = 1000,
    chunk_overlap = 200
)

chunks = splitter.split_documents(docs)


# create the embeddings
embedding_client = OpenAIEmbeddings()



# store into chroma
vectorestore = Chroma.from_documents(
    documents=chunks,
    embedding=embedding_client,
    persist_directory="chroma_db"
)




