from typing_extensions import TypedDict
from typing import Annotated
from langgraph.graph.message import add_messages
from langgraph.graph import StateGraph, START, END
from langchain.chat_models import init_chat_model
from langgraph.checkpoint.mongodb import MongoDBSaver
from dotenv import load_dotenv


load_dotenv()


llm = init_chat_model(model="gpt-4.1-mini", model_provider="openai")


class State(TypedDict):
    messages: Annotated[list, add_messages]


def chatbot(state: State):
    response = llm.invoke(state.get("messages"))
    return {"messages": [response]}


graph_builder = StateGraph(State)

graph_builder.add_node("chatbot", chatbot)


graph_builder.add_edge(START, "chatbot")
graph_builder.add_edge("chatbot", END)


# Graph with no checkpointing
graph = graph_builder.compile()


# Returns a graph with checkpointing
DB_URI = "mongodb://admin:admin@localhost:27017"


def compile_graph_with_checkpointer(checkpointer):
    return graph_builder.compile(checkpointer=checkpointer)


with MongoDBSaver.from_conn_string(DB_URI) as checkpointer:
    graph_with_checkpointer = compile_graph_with_checkpointer(checkpointer=checkpointer)

    config = {"configurable": {"thread_id": "aneesh"}}

    # With invoke it become very difficult to read the actual content as it returns everything (msg, token, cost etc...)
    # updated_state = graph_with_checkpointer.invoke(
    #     State({"messages": ["What is my name?"]}), config
    # )
    # print("\n\nupdated_state", updated_state)



    # So we'll be using .stream() instead
    for chunk in graph_with_checkpointer.stream(
        State({"messages": ["What am I learning?"]}), config,
        stream_mode="values"
    ):
        chunk["messages"][-1].pretty_print()



"""
Checkpointer (aneesh) = Hey, My name is Aneesh Paul

So every chat msg is now mapped to (aneesh)
If you just change it in the config to something different, then run the file
You won't be able to see the msg or knowledge base mapped to (aneesh)

"""
