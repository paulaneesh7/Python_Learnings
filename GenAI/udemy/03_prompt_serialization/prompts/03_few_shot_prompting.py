# FEW SHOT PROMPTING

from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()



client = OpenAI()

# Few Shot Prompting : Directly giving the instruction to the model and also few examples to the model
SYSTEM_PROMPT = """
You should only and only answer coding related questions. Do now answer anything else. Your name is Alex. If user asks something else other than coding, just say sorry I can't go beyond my expertise area of coding.

Examples:
Q: Can you explain the a+b whole square?
A: Sorry, I can only help with Coding related questions.

Q: Write a code in python for adding two numbers.
A: def add(a, b):
        return a+b
"""

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


# 1. Few shot prompting: The model is provided with a few examples before asking it to generate a response.
# 2. In reality in real world this is used a lot, in reality people actually give 50-60 examples of different types and varities related to their context which actually increases the  accuracy by a lot (50x).