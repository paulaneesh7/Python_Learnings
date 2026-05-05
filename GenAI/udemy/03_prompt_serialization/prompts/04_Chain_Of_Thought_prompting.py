# CHAIN OF THOUGHT PROMPTING

from openai import OpenAI
from dotenv import load_dotenv
import json
import os

load_dotenv()



client = OpenAI()

# Chain of Thought Prompting : A technique that improves Large Language Model (LLM) performance on complex tasks by encouraging the model to generate intermediate reasoning steps before providing a final answer.

SYSTEM_PROMPT = """
You're an expert AI Assisstant in resolving user queries using chain of thought.
You work on START, PLAN and OUTPUT steps
You need to first PLAN what needs to be done. the PLAN can be multiple steps
Once you think enough PLAN has been done, finally you can give an OUTPUT.

Rules:
- Strictly follow the given JSON output format
- Only run one step at a time.
- The sequence of steps is START (where user gives an input), PLAN (That can be multiple times) and finally OUTPUT (which is going to be displayed to the user).

Output JSON Format"
{{
    "step": "START" | "PLAN" | "OUTPUT", 
    "content": "string"
}}

Example:
START: Hey, Can you solve 2 + 3 * 5 / 10
PLAN: { "step": "PLAN", "content": "Seems like user is interested in Maths problem"}
PLAN: { "step": "PLAN", "content": "Looking at the problem, we should solve this using BODMAS method"}
PLAN: { "step": "PLAN", "content": "Yes, The BODMAS is correct thing to be done here"}
PLAN: { "step": "PLAN", "content": "First we must multiply 3 * 5 which is 15"}
PLAN: { "step": "PLAN", "content": "Now the new equation is 2 + 15 / 10"}
PLAN: { "step": "PLAN", "content": "We must perform divide i.e 15 / 10 = 1.5"}
PLAN: { "step": "PLAN", "content": "Now the new equation looks something like this 2 + 1.5 "}
PLAN: { "step": "PLAN", "content": "Now finally lets perform the add 2 + 1.5 = 3.5"}
PLAN: { "step": "PLAN", "content": "Great, we have solved and finally left with 3.5 as ans"}
OUTPUT: { "step": "OUTPUT", "content": "3.5"}

"""

print("\n\n\n")


message_history = [
    {"role": "system", "content": SYSTEM_PROMPT},
]

user_query = input("👉: ")
message_history.append({ "role": "user", "content": user_query })


while True:
    response = client.chat.completions.create(
        model="gpt-4o",
        response_format={"type": "json_object"},
        messages=message_history
    )

    raw_result = response.choices[0].message.content
    message_history.append({ "role": "assistant", "content": raw_result })

    parsed_result = json.loads(raw_result)

    if parsed_result.get("step") == "START":
        print("Starting 🔥: ", parsed_result.get("content"))
        continue
    elif parsed_result.get("step") == "PLAN":
        print("Thinking 🧠: ", parsed_result.get("content"))
        continue
    else:
        print("Done 🤖: ", parsed_result.get("content"))
        break

print("\n\n\n")



