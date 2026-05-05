from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader



loader = DirectoryLoader(
    path='sample_docs',
    glob='*pdf',
    loader_cls=PyPDFLoader
)


docs = loader.lazy_load()



for doc in docs:
    print(doc.metadata)