import requests
from google.colab import userdata

# LangChain imports
from langchain_openai import ChatOpenAI
from langchain_core.tools import tool
from langchain_community.tools import DuckDuckGoSearchRun
from langchain.agents import create_agent


# ============================================
# STEP 1 — LLM SETUP
# ============================================

OPENAI_API_KEY = userdata.get("OPENAI_API_KEY")

llm = ChatOpenAI(
    model="gpt-4o-mini",
    api_key=OPENAI_API_KEY,
    temperature=0
)


# ============================================
# STEP 2 — SEARCH TOOL
# ============================================

search_tool = DuckDuckGoSearchRun()


# ============================================
# STEP 3 — CUSTOM TOOL
# ============================================

@tool
def get_weather_data(city: str) -> str:
    """
    Fetch current weather data for a city
    """

    url = f"https://wttr.in/{city}?format=j1"

    response = requests.get(url)

    data = response.json()

    current = data["current_condition"][0]

    return f"""
    City: {city}
    Temperature: {current['temp_C']}°C
    Humidity: {current['humidity']}%
    Weather: {current['weatherDesc'][0]['value']}
    """


# ============================================
# STEP 4 — TOOL LIST
# ============================================

tools = [
    search_tool,
    get_weather_data
]


# ============================================
# STEP 5 — CREATE AGENT
# ============================================

agent = create_agent(
    model=llm,
    tools=tools,
    system_prompt="""
    You are a helpful AI assistant.

    Use tools whenever required.
    Give concise and accurate answers.
    """
)


# ============================================
# STEP 6 — INVOKE AGENT
# ============================================

response = agent.invoke({
    "messages": [
        {
            "role": "user",
            "content": "What's the weather in Kolkata today?"
        }
    ]
})

final_answer = response["messages"][-1].content

print(final_answer)