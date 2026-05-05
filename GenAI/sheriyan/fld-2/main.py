from dotenv import load_dotenv
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_openai import ChatOpenAI
from langchain_mistralai import ChatMistralAI
from langchain_core.prompts import ChatPromptTemplate


load_dotenv()


embedding_client = OpenAIEmbeddings()


docs = PyPDFLoader("cs_sample.pdf").load()



splitter = RecursiveCharacterTextSplitter(
    chunk_size = 1000,
    chunk_overlap = 200
)

chunks = splitter.split_documents(docs)






vectorestore = Chroma.from_documents(
    documents=chunks,
    embedding=embedding_client,
    persist_directory="chroma_db"
)



retriever = vectorestore.as_retriever(
    search_type="mmr",
    search_kwargs = {
        "k": 4,
        "fetch_k": 10,
        "lambda_mult": 0.5
    }
)


llm = ChatMistralAI(
    model="mistral-small-2506"
)



# Prompt Template

prompt = ChatPromptTemplate.from_messages(
    [
        ("system",  """You are a helpful AI assistant.

Use ONLY the provided context to answer the question.

If the answer is not present in the context,
say: "I could not find the answer in the document."
"""),

    (
        "human",
        """Context:

        {context}
Question:
{question}
"""
    )
    ]
)


print("\n\nRag System Created\n\n")


print("Press 0 to exit")

while True:
    query = input("User >: ")
    if query == "0":
        break

    docs = retriever.invoke(query)

    context = "\n\n".join([doc.page_content for doc in docs])

    final_prompt = prompt.invoke({
        "context": context,
        "question": query
    })

    response = llm.invoke(final_prompt)

    print(f"\n AI: {response.content}")


