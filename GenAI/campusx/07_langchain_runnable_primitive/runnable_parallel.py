from langchain_openai import ChatOpenAI
from langchain_core.runnables import RunnableSequence, RunnableParallel
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv


load_dotenv()

# We are using same model here for parallel execution, but you can use different models for each prompt if you want to.
model = ChatOpenAI(
    model="gpt-4.1"
)


parser = StrOutputParser()


prompt1 = PromptTemplate(
    template="Generate a tweet about {topic}",
    input_variables=["topic"]
)


prompt2 = PromptTemplate(
    template="Generate a LinkedIn post about {topic}",
    input_variables=["topic"]
)


parallel_chain = RunnableParallel({
    'tweet': RunnableSequence(prompt1, model, parser),
    'linkedin': RunnableSequence(prompt2, model, parser)
})


result = parallel_chain.invoke({
    "topic": "AI"
})


# As runnable parallel returns a dictionary, we can access the results using the keys we defined in the RunnableParallel constructor.
print("🥂 Tweet:", result['tweet'])
print("🔥 LinkedIn Post:", result['linkedin'])


