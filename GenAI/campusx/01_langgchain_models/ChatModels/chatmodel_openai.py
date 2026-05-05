from langchain_openai import ChatOpenAI
from dotenv import load_dotenv



load_dotenv()


model = ChatOpenAI(
    model="gpt-4.1",
    temperature=0.7,
    max_completion_tokens=10
)


response = model.invoke("Write a 3 lines humorous poem for football")

print(response.content)