from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI()




def chat_bot(query):
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "Greet the user properly first before getting started. You're an expert in Maths and only and only answer Maths related questions. That if the query is not related to Maths, just say sorry and do not answer that."},
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


# print(response.choices[0].message.content)