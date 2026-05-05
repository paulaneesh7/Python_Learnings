import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from pydantic import BaseModel
from typing import List, Optional
from langchain_core.output_parsers import PydanticOutputParser


load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")


class Movie(BaseModel):
    title: str
    release_year: Optional[int]
    genre: List[str]
    director: Optional[str]
    cast: List[str]
    rating: Optional[float]
    awards: Optional[List[str]]
    summary: str


# This parser will check whether the information is actually in the correct format or not
parser = PydanticOutputParser(pydantic_object=Movie)


client = ChatOpenAI(
    model="gpt-4.1",
    temperature=0.2
)

extraction_prompt = ChatPromptTemplate.from_messages([
    ("system", """
    Extract movie information from the paragraph
     {format_instructions}
"""),
("human", "{paragraph}")
])

para = input("Enter the paragraph you want to extract info from: ")

FINAL_PROMPT = extraction_prompt.invoke(
    {"paragraph": para,
    "format_instructions": parser.get_format_instructions()
    }
)

response = client.invoke(FINAL_PROMPT)

movie_data = parser.parse(response.content)

print(movie_data) 