import requests
from google.colab import userdata

# ============================================
# LANGCHAIN IMPORTS
# ============================================

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

    print(f"\n🌦️ TOOL EXECUTING: get_weather_data('{city}')")

    url = f"https://wttr.in/{city}?format=j1"

    response = requests.get(url)

    data = response.json()

    current = data["current_condition"][0]

    result = f"""
    City: {city}
    Temperature: {current['temp_C']}°C
    Humidity: {current['humidity']}%
    Weather: {current['weatherDesc'][0]['value']}
    """

    print("\n✅ TOOL RESULT:")
    print(result)

    return result


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
# STEP 6 — USER QUERY
# ============================================

user_query = "What's the weather in Kolkata today?"


# ============================================
# STEP 7 — STREAM AGENT EXECUTION
# ============================================

print("\n==============================")
print("🚀 AGENT EXECUTION STARTED")
print("==============================\n")


final_response = None

for step in agent.stream(
    {
        "messages": [
            {
                "role": "user",
                "content": user_query
            }
        ]
    },
    stream_mode="values"
):

    last_message = step["messages"][-1]

    print("\n-----------------------------------")
    print(f"🧠 MESSAGE TYPE: {last_message.type}")
    print("-----------------------------------")


    # ============================================
    # TOOL CALLS
    # ============================================

    if hasattr(last_message, "tool_calls") and last_message.tool_calls:

        print("\n🔧 TOOL CALLS:")

        for tool_call in last_message.tool_calls:
            print(f"\nTool Name: {tool_call['name']}")
            print(f"Arguments: {tool_call['args']}")


    # ============================================
    # MESSAGE CONTENT
    # ============================================

    if last_message.content:
        print("\n💬 CONTENT:")
        print(last_message.content)


    final_response = last_message


# ============================================
# STEP 8 — FINAL ANSWER
# ============================================

print("\n===================================")
print("✅ FINAL ANSWER")
print("===================================\n")

print(final_response.content)