import os
from dotenv import load_dotenv
from langchain_openai import OpenAIEmbeddings



load_dotenv()


embedding_client = OpenAIEmbeddings(
    model="text-embedding-3-large",
    dimensions=64
)



"""
embed_documents() : When the content is huge (multiple sentences)
embed_query() : When the content is just a simple sentence
"""
vector1 = embedding_client.embed_query("Hey! Lets start learning Gen-AI")

# print(vector1)


texts = [
    "Hello, this is Aneesh Paul",
    "Currently working as a Software Engineer in TCS",
    "I am very much enthusiast in Tech and AI industry"
]


vector2 = embedding_client.embed_documents(texts)

print(vector2)
