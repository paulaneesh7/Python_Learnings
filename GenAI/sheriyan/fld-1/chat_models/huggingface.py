import os
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv

load_dotenv()

HUGGINGFACE_HUB_ACCESS_TOKEN = os.getenv("HUGGINGFACE_HUB_ACCESS_TOKEN")

client = HuggingFaceEndpoint(
    repo_id="deepseek-ai/DeepSeek-R1-Distill-Qwen-7B",
    task="text-generation",
    huggingfacehub_api_token=HUGGINGFACE_HUB_ACCESS_TOKEN
)
    
model = ChatHuggingFace(llm=client)

response = model.invoke("Who're you?")

print(response.content)
