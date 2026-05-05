from langchain_community.document_loaders import TextLoader, PyPDFLoader
from langchain_text_splitters import CharacterTextSplitter, TokenTextSplitter, RecursiveCharacterTextSplitter


text_splitter = RecursiveCharacterTextSplitter(
    chunk_size = 100,
    chunk_overlap = 40
)


data = PyPDFLoader("cs_sample.pdf").load()


chunks = text_splitter.split_documents(data)

print(len(chunks))
print(chunks[0])