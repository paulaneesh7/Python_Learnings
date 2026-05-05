from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings
from langchain_core.documents import Document
from dotenv import load_dotenv



load_dotenv()




docs = [
    Document(page_content="Python is widely used in Artificial Intelligence.", metadata={"source": "AI_book"}),
    Document(page_content="JavaScript is already very much used and is quite well adopted through its frameworks.", metadata={"source": "JavaScript Enclycopedia"}),
    Document(page_content="Rust is getting very popular lately in building low level and kernel lvl applications even adopted by top product based firms.", metadata={"source": "Rust Handbook"}),
]


embedding_client = OpenAIEmbeddings()

vectorstore = Chroma.from_documents(
    documents=docs,
    embedding=embedding_client,
    persist_directory="chroma_db"
)



results = vectorstore.similarity_search("What is used for Artificial Intelligence", k=2)


for r in results:
    print(r)


retriever = vectorstore.as_retriever()

docs = retriever.invoke("Explain kernel lvl applications")

for d in docs:
    print(d.page_content)





