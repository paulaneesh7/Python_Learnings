# CHAIN OF THOUGHT PROMPTING

from openai import OpenAI
from dotenv import load_dotenv
from pydantic import BaseModel, Field
from typing import Optional
import json
import os
import requests

load_dotenv()



client = OpenAI()



def get_weather(city:str):
    url = f"https://wttr.in/{city.lower()}?format=3"

    response = requests.get(url)

    if response.status_code == 200:
        return f"The weather in {city} is {response.text}"
    
    return "Something went wrong"


def run_command(cmd: str):
    result = os.system(cmd)
    return result


available_tools = {
    "get_weather": get_weather,
    "run_command": run_command
}



# Chain of Thought Prompting : A technique that improves Large Language Model (LLM) performance on complex tasks by encouraging the model to generate intermediate reasoning steps before providing a final answer.
SYSTEM_PROMPT = """
You're an expert AI Assisstant in resolving user queries using chain of thought.
You work on START, PLAN and OUTPUT steps
You need to first PLAN what needs to be done. the PLAN can be multiple steps
Once you think enough PLAN has been done, finally you can give an OUTPUT.
You can also call a tool if required from the list of available tools.
For every tool call wait for the observe step which is the output from the called tool.

Rules:
- Strictly follow the given JSON output format
- Only run one step at a time.
- The sequence of steps is START (where user gives an input), PLAN (That can be multiple times) and finally OUTPUT (which is going to be displayed to the user).

Output JSON Format"
{{
    "step": "START" | "PLAN" | "OUTPUT" | "TOOL", 
    "content": "string",
    "tool": "string",
    "input": "string"
}}

Available Tools:
- get_weather: Takes city name as an input string and returns the weather information about the city.
- run_command: Takes a system linux command as string and executes the command on user's system and returns the output from the command.

Example1:
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



Example2:
START: What is the weather of Delhi?
PLAN: { "step": "PLAN", "content": "Seems like user is interested in getting weather of Delhi in india"}
PLAN: { "step": "PLAN", "content": "Lets see if we have any available tool from the list of available tools"}
PLAN: { "step": "PLAN", "content": "Great, we have get_weather tool avilable for this query"}
PLAN: { "step": "PLAN", "content": "I need to call get_weather tool for Delhi as input for city"}
PLAN: { "step": "TOOL", "tool": "get_weather", "input": "Delhi"}
PLAN: { "step": "OBSERVE", "tool": "get_weather", "input": "The temp of Delhi is cloudy with 20deg celcius"}
PLAN: { "step": "PLAN", "content": "Great I got the weather info about Delhi"}
OUTPUT: { "step": "OUTPUT", "content": "The current weather in Delhi is 20 degree celcius with some cloud sky."}

"""

print("\n\n\n")


class MyOutputFormat(BaseModel):
    step: str = Field(
        ...,
        description="The ID of the step. Example: PLAN, OUTPUT, TOOL etc..."
    )
    content: Optional[str] = Field(
        None,
        description="The optional string content for the step."
    )
    tool: Optional[str] = Field(
        None,
        description="The ID of the tool to call."
    )
    input: Optional[str] = Field(
        None,
        description="The input params for the tool."
    )


message_history = [
    {"role": "system", "content": SYSTEM_PROMPT},
]

while True:

    user_query = input("👉: ")
    message_history.append({ "role": "user", "content": user_query })


    while True:
        response = client.chat.completions.parse(
            model="gpt-4o",
            response_format=MyOutputFormat,
            messages=message_history
        )

        raw_result = response.choices[0].message.content
        message_history.append({ "role": "assistant", "content": raw_result })

        # This will give a parsed result directly, so no need to do json.loads()
        parsed_result = response.choices[0].message.parsed

        if parsed_result.step == "START":
            print("Starting 🔥: ", parsed_result.content)
            continue
        elif parsed_result.step == "TOOL":
            tool_to_call = parsed_result.tool
            tool_input = parsed_result.input
            print(f"Wizard: {tool_to_call} ({tool_input})")

            tool_response = available_tools[tool_to_call](tool_input)
            print(f"Checking result: {tool_to_call} ({tool_input}) = {tool_response}")
            message_history.append({ "role": "developer", "content": json.dumps(
                { "step": "OBSERVE", "tool": tool_to_call, "input": tool_input, "output": tool_response }
            ) })
            continue

        elif parsed_result.step == "PLAN":
            print("Thinking 🧠: ", parsed_result.content)
            continue
        else:
            print("Done 🤖: ", parsed_result.content)
            break

    print("\n\n\n")



