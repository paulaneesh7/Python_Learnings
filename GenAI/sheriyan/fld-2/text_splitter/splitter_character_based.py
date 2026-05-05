from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import CharacterTextSplitter


text_splitter = CharacterTextSplitter(
    chunk_size = 10,
    chunk_overlap = 4
)


data = TextLoader("sample.txt").load()


chunks = text_splitter.split_documents(data)

print(len(chunks))
print(chunks)