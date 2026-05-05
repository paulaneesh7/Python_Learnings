from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

client = OpenAI(
    api_key=api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

# response = client.chat.completions.create(
#     model="gemini-3-flash-preview",
#     messages=[
#         {   "role": "system",
#             "content": "You are a helpful assistant."
#         },
#         {
#             "role": "user",
#             "content": "Explain to me how AI works"
#         }
#     ]
# )


response = client.chat.completions.create(
    model="gemini-3-flash-preview",
    messages=[
        {
            "role": "user",
            "content": "Hey, I am Aneesh Paul! Nice to meet you. Who're you?"
        }
    ]
)

print(response.choices[0].message.content)