from dotenv import load_dotenv
from langchain_mistralai import ChatMistralAI
from langchain_community.document_loaders import TextLoader, PyPDFLoader
from langchain_text_splitters import CharacterTextSplitter, TokenTextSplitter
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()

data = PyPDFLoader("cs_sample.pdf").load()


text_splitter = TokenTextSplitter(
    chunk_size = 1000,
    chunk_overlap = 400
)


template = ChatPromptTemplate(
    [
        ("system", "You're an AI agent that summarizes the text"),
        ("human", "{data}")
    ]
)

chunks = text_splitter.split_documents(data)

model = ChatMistralAI(
    model="mistral-small-2506"
)

prompt = template.format_messages(data=data)

results = model.invoke(prompt)

print(results.content)
