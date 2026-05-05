from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv


load_dotenv()

documents = [
    "New Delhi is the capital of India",
    "Moscow is the capital of Russia",
    "Tokyo is the capital of Japan",
    "Seoul is the capital of South Korea"
]


embedding_model = OpenAIEmbeddings(
    model="text-embedding-3-large",
    dimensions=32
)



response = embedding_model.embed_documents(documents)

print(str(response))