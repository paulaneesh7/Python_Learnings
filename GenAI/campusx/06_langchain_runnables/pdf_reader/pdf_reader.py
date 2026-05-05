from langchain.document_loader import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.llms import OpenAI


#  Load the document
loader = TextLoader("example.pdf")
documents = loader.load()



# Split the text into smaller chunks
text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
docs = text_splitter.split_documents(documents)



# Convert text into embeddings & store in FAISS
vectorestore = FAISS.from_documents(docs, OpenAIEmbeddings())


# Create a retriever (fetches relevant documents)
retriever = vectorestore.as_retriever()



# Manually Retrieve Relevant Documents
query = "What are the key takeaways from the document?"
retrieved_docs = retriever.get_relevant_documents(query)


# Combine Retrieved Text into a Single Prompt
llm = OpenAI(
    model_name = "gpt-3.5-turbo",
    temperature = 0.7
)


# Manually Pass Retrieved Text to LLM
prompt = f"Based on the following text, answer the questions: {query}\n\n{retrieved_docs}"
answer = llm.predict(prompt)


# Print the Answer
print("Answer:", answer)