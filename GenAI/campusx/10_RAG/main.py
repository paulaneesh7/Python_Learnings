from youtube_transcript_api import YouTubeTranscriptApi, TranscriptsDisabled
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_community.vectorstores import FAISS
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableParallel, RunnablePassthrough, RunnableLambda
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv


load_dotenv()

embeddings = OpenAIEmbeddings(model="text-embedding-3-small")

llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.2)

video_id = "Gfr50f6ZBvo"

try:
    ytt_api = YouTubeTranscriptApi()

    transcript_list = ytt_api.fetch(video_id, languages=["en"])

    transcript = " ".join(chunk.text for chunk in transcript_list)

except TranscriptsDisabled:
    print("No captions available for this video.")
    

splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
chunks = splitter.create_documents([transcript])


vector_store = FAISS.from_documents(chunks, embeddings)



retriever = vector_store.as_retriever(search_type="similarity", search_kwargs={"k": 4})


question = "is the topic of nuclear fusion discussed in this video? if yes then what was discussed"
retrieved_docs    = retriever.invoke(question)
prompt = PromptTemplate(
    template="""
      You are a helpful assistant.
      Answer ONLY from the provided transcript context.
      If the context is insufficient, just say you don't know.

      {context}
      Question: {question}
    """,
    input_variables = ['context', 'question']
)

context_text = "\n\n".join(doc.page_content for doc in retrieved_docs)


# Final Prompt
final_prompt = prompt.invoke({"context": context_text, "question": question})

answer = llm.invoke(final_prompt)

def format_docs(retrieved_docs):
  context_text = "\n\n".join(doc.page_content for doc in retrieved_docs)
  return context_text


parallel_chain = RunnableParallel({
    'context': retriever | RunnableLambda(format_docs),
    'question': RunnablePassthrough()
})


parallel_chain.invoke('who is Demis')

parser = StrOutputParser()


main_chain = parallel_chain | prompt | llm | parser


result = main_chain.invoke('Can you summarize the video')

print(result)