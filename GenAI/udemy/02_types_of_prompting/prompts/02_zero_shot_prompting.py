# ZERO SHOT PROMPTING

from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()



client = OpenAI()

# Zero Shot Prompting : Directly giving the instruction to the model
SYSTEM_PROMPT = "You should only and only answer coding related questions. Do now answer anything else. Your name is Alex. If user asks something else other than coding, just say sorry I can't go beyond my expertise area of coding."

def chat_bot(query):
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": query}
        ]
    )

    return response.choices[0].message.content


while True:
    query = input("Enter your query: ")
    ans = chat_bot(query)
    print(ans)
    inp = input("Do you wanna continue (Y/N):")
    
    if inp == 'N':
        break


# 1. Zero shot prompting: The model is given a direct question or task without prior examples.