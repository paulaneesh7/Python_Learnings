from langchain_community.document_loaders import WebBaseLoader


URL = "https://www.apple.com/macbook-pro/"

data = WebBaseLoader(URL)
docs = data.load()

print(len(docs))

print(docs[0].page_content)