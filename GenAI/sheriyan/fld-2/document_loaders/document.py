from langchain_community.document_loaders import TextLoader


data = TextLoader("sample.txt")

docs = data.load()

print(docs[0])