from dotenv import load_dotenv
from langchain_mistralai import ChatMistralAI
from langchain_community.document_loaders import TextLoader, PyPDFLoader
from langchain_text_splitters import CharacterTextSplitter, TokenTextSplitter
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()







template = ChatPromptTemplate(
    [
        ("system", "You're an AI agent that summarizes the text"),
        ("human", "{data}")
    ]
)



model = ChatMistralAI(
    model="mistral-small-2506"
)


