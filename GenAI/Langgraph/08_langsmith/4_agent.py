from langchain_openai import ChatOpenAI
from langchain_core.tools import tool
import requests
from langchain_community.tools import DuckDuckGoSearchRun
from langchain.agents import create_agent
from dotenv import load_dotenv

load_dotenv()

# LANGSMITH_PROJECT="Langchain-Demo-04-ReAct-Agent"

search_tool = DuckDuckGoSearchRun()

@tool
def get_weather_data(city: str) -> str:
  """
  This function fetches the current weather data for a given city.
  """
  url = f'https://api.weatherstack.com/current?access_key=f07d9636974c4120025fadf60678771b&query={city}'

  response = requests.get(url)

  return response.json()

llm = ChatOpenAI()

agent = create_agent(
    model=llm,
    tools=[search_tool, get_weather_data],
    system_prompt="You are a helpful assistant that can use tools to answer the user's questions."
)

# What is the release date of Dhadak 2?
# What is the current temp of gurgaon?
# Identify the birthplace city of Kalpana Chawla (search) and give its current temperature.

response = agent.invoke({
    "messages": [{"role": "user", "content": "What is the release date of Avengers Doomsday?"}]
})

print(response)

try:
    print(response["output"])
except Exception:
    pass