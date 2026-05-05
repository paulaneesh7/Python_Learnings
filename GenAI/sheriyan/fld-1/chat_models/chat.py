import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_groq import ChatGroq
from langchain_mistralai import ChatMistralAI

load_dotenv()


OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
MISTRAL_API_KEY = os.getenv("MISTRAL_API_KEY")


# client = ChatOpenAI(model="gpt-4.1")

"""
Temperature range is between 0-1

If you want to write a poem, temp should be closer to 1
If you want to use the model for some mathematical calculations or for some highly specific work, temp should be reduced

Basically for creative task : Increase temperature
For logical task: Decrease temperature
"""
client = ChatMistralAI(
    model="mistral-small-2506", 
    temperature=0.2,
    max_tokens=20
)


response = client.invoke("Write a poem on AI")

print(response.content)