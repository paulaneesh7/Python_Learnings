import streamlit as st
from langgraph_tool_backend import chatbot, retrieve_all_threads
from langchain_core.messages import HumanMessage, AIMessage, ToolMessage
import uuid





# ******************************************************************** Utility Function *************************************************************

def generate_thread_id():
    thread_id = uuid.uuid4()
    
    return thread_id


# Basically create a new thread_id for new chat and also empty the previous chat msg history
def reset_chat():
    thread_id = generate_thread_id()
    
    st.session_state['thread_id'] = thread_id
    add_thread(st.session_state['thread_id'])
    st.session_state['message_history'] = []



# To add thread_id to chat_threads
def add_thread(thread_id):
    if thread_id not in st.session_state['chat_threads']:
        st.session_state['chat_threads'].append(thread_id)




# Returns the entire message stored inside that particular thread
def load_conversation(thread_id):
    return chatbot.get_state(config={'configurable': {'thread_id': thread_id}}).values['messages']




# ****************************************************************** Session Setup ************************************************************

if 'message_history' not in st.session_state:
    st.session_state['message_history'] = []


# if thread_id is not present in session, then generate thread_id
if 'thread_id' not in st.session_state:
    st.session_state['thread_id'] = generate_thread_id()
    

# Basically to store all the thread_ids for every chat
if 'chat_threads' not in st.session_state:
    st.session_state['chat_threads'] = retrieve_all_threads()
    
    
add_thread(st.session_state['thread_id'])

# ****************************************************************** Sidebar UI ************************************************************


st.sidebar.title("LangGraph Chatbot")


if st.sidebar.button("New Chat"):
    reset_chat()


st.sidebar.header("My Conversation")

for thread_id in st.session_state['chat_threads'][::-1]:
    if st.sidebar.button(str(thread_id)):
        st.session_state['thread_id'] = thread_id
        messages = load_conversation(thread_id)
        
        temp_messages = []
        
        for msg in messages:
            if isinstance(msg, HumanMessage):
                role = 'user'
            else:
                role = 'assistant'
            temp_messages.append({'role': role, 'content': msg.content})
        
        
        st.session_state['message_history'] = temp_messages

# ****************************************************************** Main UI ************************************************************


# loading the conversation history
for message in st.session_state['message_history']:
    with st.chat_message(message['role']):
        st.text(message['content'])




user_input = st.chat_input('Type here')

if user_input:

    # first add the message to message_history
    st.session_state['message_history'].append({'role': 'user', 'content': user_input})
    with st.chat_message('user'):
        st.text(user_input)
        
    
    
    
    
    CONFIG = {
        "configurable": {"thread_id": st.session_state["thread_id"]},
        "metadata": {
            "thread_id": st.session_state["thread_id"]
        },
        "run_name": "chat_turn",
    }


    # (Newly Added)
    # Assistant streaming block
    with st.chat_message("assistant"):
        # Use a mutable holder so the generator can set/modify it
        status_holder = {"box": None}

        def ai_only_stream():
            for message_chunk, metadata in chatbot.stream(
                {"messages": [HumanMessage(content=user_input)]},
                config=CONFIG,
                stream_mode="messages",
            ):
                # Lazily create & update the SAME status container when any tool runs
                if isinstance(message_chunk, ToolMessage):
                    tool_name = getattr(message_chunk, "name", "tool")
                    if status_holder["box"] is None:
                        status_holder["box"] = st.status(
                            f"🔧 Using `{tool_name}` …", expanded=True
                        )
                    else:
                        status_holder["box"].update(
                            label=f"🔧 Using `{tool_name}` …",
                            state="running",
                            expanded=True,
                        )

                # Stream ONLY assistant tokens
                if isinstance(message_chunk, AIMessage):
                    yield message_chunk.content

        ai_message = st.write_stream(ai_only_stream())

        # Finalize only if a tool was actually used
        if status_holder["box"] is not None:
            status_holder["box"].update(
                label="✅ Tool finished", state="complete", expanded=False
            )

    # Save assistant message
    st.session_state["message_history"].append(
        {"role": "assistant", "content": ai_message}
    )