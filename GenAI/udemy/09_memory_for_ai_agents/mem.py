from mem0 import Memory
from dotenv import load_dotenv
from openai import OpenAI
import os
import json

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")


client = OpenAI()

# Config for mem0
config = {
    "version": "v1.1",
    "embedder": {
        "provider": "openai",
        "config": {
            "api_key": OPENAI_API_KEY,
            "model": "text-embedding-3-small"
        }
    },
    "llm": {
        "provider": "openai",
        "config": {
            "api_key": OPENAI_API_KEY,
            "model": "gpt-4.1"
        }
    },
    "vector_store": {
        "provider": "qdrant",
        "config": {
            "host": "localhost",
            "port": 6333
        }
    }
}

# ✅ Correct initialization
memory = Memory.from_config(config)

while True:


    user_query = input("Enter: ")
    
    
    # It is going to find only relevant memories (not all memories)
    search_memory = memory.search(query=user_query, filters={"user_id": "paulaneesh"})
    
    
    memories = [
        f"ID: {mem.get("id")}\nMemory: {mem.get("memory")}" 
        for mem in search_memory.get("results")
    ]
    
    print(f"Found memories: {memories}")
    
    
    SYSTEM_PROMPT = f"""
        Here is the context about the user:
        {json.dumps(memories)}
    """


    response = client.chat.completions.create(
        model="gpt-4.1",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": user_query}
        ]
    )

    result = response.choices[0].message.content

    print(f"AI: {result}")

    # Save to memory
    memory.add(
        user_id="paulaneesh",
        messages=[
            {"role": "user", "content": user_query},
            {"role": "assistant", "content": result}
        ]
    )

    print("Memory has been saved")