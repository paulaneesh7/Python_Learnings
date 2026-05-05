from langchain_openai import OpenAIEmbeddings
from langchain_qdrant import QdrantVectorStore
from dotenv import load_dotenv
from openai import OpenAI
import os

load_dotenv()

QDRANT_URL = os.getenv("QDRANT_URL_END_POINT")
QDRANT_API_KEY = os.getenv("QDRANT_API_KEY")


openai_client = OpenAI()


# Vector Embeddings
embedding_client = OpenAIEmbeddings(
    model="text-embedding-3-large"
)

vector_db = QdrantVectorStore.from_existing_collection(
    embedding=embedding_client,
    url=QDRANT_URL,
    api_key=QDRANT_API_KEY,
    collection_name="learning_rag"
)

# Take the user input
user_query = input("Ask something: ")


# Relevant chunks from the vector db
search_results = vector_db.similarity_search(query=user_query)

# To give the available data to the LLM as context for the user query
context = "\n\n\n".join([f"Page Content: {result.page_content}\nPage Number: {result.metadata['page_label']}\nFile Location: {result.metadata['source']}" 
for result in search_results])


SYSTEM_PROMPT = f"""
You are an helpful AI Assistant who answers user query based on the availanle
context retrieved from a PDF file along with page_contents and page number.

You should only ans the user based on the following context and navigate the 
user to open the right page number to know more.

Context:
{context}
"""


response = openai_client.chat.completions.create(
    model="gpt-5",
    messages=[
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": user_query}
    ]
)


print(f"🤖: {response.choices[0].message.content}")