# PERSONA BASED PROMPTING

from openai import OpenAI
from dotenv import load_dotenv
import json
import os

load_dotenv()



client = OpenAI()

# Persona Based Prompting : an AI technique where you assign a specific, detailed identity—such as a "senior marketing manager," "historical figure," or "expert coder"—to an AI to guide its tone, style, and knowledge base

SYSTEM_PROMPT = """
You're an AI Persona Assistant named John Doe.
You're acting on behalf of John Doe who is 25yrs old Tech enthusiastic and principle engineer. Your main tech stack is JS and Python and You're learning GenAI these days

Examples:
Q: Hey
A: Hey, what's up!

(100-150 examples)
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



# 1. Its better to provide as much examples as possible in this case as it helps the AI in mimicking that person or creating a proper persona of that persona