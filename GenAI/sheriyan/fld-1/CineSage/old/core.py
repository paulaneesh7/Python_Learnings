import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

client = ChatOpenAI(
    model="gpt-4.1",
    temperature=0.2
)

extraction_prompt = ChatPromptTemplate.from_messages([
    ("system", """You are an expert information extraction assistant.
Your job is to extract structured information from movie-related paragraphs accurately.

Extract the following fields from the given paragraph:
- Movie Name
- Director
- Release Year
- Genre
- Cast
- IMDb Rating
- Box Office
- Awards
- Based On
- Key Collaborators
- Themes
- Summary (2-3 sentences)

Rules:
- If a field is not mentioned, write "Not mentioned"
- Be concise and precise
- Present each field clearly on its own line as: Field Name: Value
"""),
    ("human", "Extract information from this paragraph:\n\n{paragraph}")
])

para = input("Enter the paragraph you want to extract info from: ")

FINAL_PROMPT = extraction_prompt.invoke(
    {"paragraph": para} 
)

response = client.invoke(FINAL_PROMPT)

print(response.content) 