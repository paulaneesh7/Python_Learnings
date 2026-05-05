from langchain_community.document_loaders import PyPDFLoader


data = PyPDFLoader("cs_sample.pdf")

docs = data.load()

print(len(docs))

print(docs[14].page_content)