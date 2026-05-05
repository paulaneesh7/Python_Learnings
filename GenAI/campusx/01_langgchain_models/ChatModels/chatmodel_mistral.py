from langchain_mistralai import ChatMistralAI
from dotenv import load_dotenv



load_dotenv()


model = ChatMistralAI(
    model="mistral-small-2506", 
    temperature=0.2,
)


response = model.invoke("Write a 3 lines humorous poem for football")

print(response.content)