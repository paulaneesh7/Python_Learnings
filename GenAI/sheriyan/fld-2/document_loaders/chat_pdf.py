import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_mistralai import ChatMistralAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_community.document_loaders import TextLoader
from langchain_community.document_loaders import PyPDFLoader


load_dotenv()


client = ChatOpenAI(
    model="gpt-4.1",
    temperature=0.2
)

model = ChatMistralAI(
    model="mistral-small-2506"
)




data = PyPDFLoader("cs_sample.pdf")

docs = data.load()


template = ChatPromptTemplate.from_messages(
    [
        ("system", "You're an AI that summarizes the text"),
        ("human", "{data}")
    ]
)

prompt = template.format_messages(data = docs[3].page_content)


response = model.invoke(prompt)
print(response.content)