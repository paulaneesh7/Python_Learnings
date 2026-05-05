import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_groq import ChatGroq
from langchain_mistralai import ChatMistralAI
from langchain_core.messages import AIMessage, SystemMessage, HumanMessage


load_dotenv()


OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
MISTRAL_API_KEY = os.getenv("MISTRAL_API_KEY")


client_mistral = ChatMistralAI(
    model="mistral-small-2506", 
    temperature=0.2,
    max_tokens=20
)

client_openai = ChatOpenAI(
    model="gpt-4.1",
    temperature=0.2
)




print("Choose your AI mode: ")
print("Press 1 for Angry mode\n Press 2 for Funny mode\n Press 3 for Sad mode")


choice = int(input("Tell your choice: "))

if choice == 1:
    mode = "You're an angry AI Agent. You response aggressively and impatiently."
elif choice == 2:
    mode = "You're a funny AI agent. You respond with humor and jokes."
elif choice == 3:
    mode = "You're a sad AI agent. You respond with sadness and sorrow."

PROMPT = f"""
{mode}
"""


messages = [
    SystemMessage(content=PROMPT)
]

print("------------Welcome type 0 to exit the application -------------")
while True: 
    user_prompt = input("Enter your prompt: ")
    messages.append(
        HumanMessage(content=user_prompt)
    )
    if user_prompt == "0":
        break


    response = client_openai.invoke(messages)
    messages.append(
        AIMessage(content=response.content)
    )
    print(f"Bot: {response.content}")


print(messages)