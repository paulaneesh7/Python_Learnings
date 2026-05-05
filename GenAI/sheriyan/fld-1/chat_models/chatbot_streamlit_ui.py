import os
from dotenv import load_dotenv
import streamlit as st
from langchain_openai import ChatOpenAI
from langchain_mistralai import ChatMistralAI
from langchain_core.messages import AIMessage, SystemMessage, HumanMessage

load_dotenv()

# ── Page config ───────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="FunnyBot",
    page_icon="🤣",
    layout="centered",
)

# ── Custom CSS ────────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&display=swap');

/* ── Global ── */
html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
    background-color: #111318;
    color: #e8e8e8;
}

#MainMenu, footer, header { visibility: hidden; }
.block-container {
    padding-top: 1.5rem;
    padding-bottom: 6rem;
    max-width: 800px;
}

/* ── Top instruction bar ── */
.top-bar {
    font-size: 0.82rem;
    color: #6b7280;
    margin-bottom: 1.4rem;
    padding-bottom: 0.6rem;
}

/* ── Message row: avatar + card ── */
.msg-row {
    display: flex;
    align-items: flex-start;
    gap: 0.85rem;
    margin-bottom: 1rem;
    animation: fadeUp 0.2s ease both;
}
@keyframes fadeUp {
    from { opacity: 0; transform: translateY(8px); }
    to   { opacity: 1; transform: translateY(0); }
}

/* ── Avatar circle ── */
.avatar {
    width: 42px;
    height: 42px;
    border-radius: 10px;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 1.3rem;
    flex-shrink: 0;
    margin-top: 2px;
}
.avatar-user { background: #c0392b; }
.avatar-bot  { background: #e67e22; }

/* ── Message card ── */
.msg-card {
    flex: 1;
    background: #1c1f26;
    border-radius: 12px;
    padding: 1.1rem 1.4rem;
    font-size: 0.97rem;
    line-height: 1.65;
    color: #e0e0e0;
    border: 1px solid #25282f;
}

/* ── Input area ── */
[data-testid="stChatInputTextArea"] textarea {
    background: #1c1f26 !important;
    color: #e0e0e0 !important;
    border: 1px solid #2e3039 !important;
    border-radius: 12px !important;
    font-family: 'Inter', sans-serif !important;
    font-size: 0.93rem !important;
    padding: 0.85rem 1.1rem !important;
}
[data-testid="stChatInputTextArea"] textarea:focus {
    border-color: #444 !important;
    box-shadow: none !important;
}

button[data-testid="stChatInputSubmitButton"] {
    background: #f9d423 !important;
    border-radius: 10px !important;
    color: #111 !important;
}

/* ── Sidebar ── */
[data-testid="stSidebar"] {
    background: #13161c !important;
    border-right: 1px solid #1e2128;
}

/* ── Scrollbar ── */
::-webkit-scrollbar { width: 4px; }
::-webkit-scrollbar-track { background: #111; }
::-webkit-scrollbar-thumb { background: #2e3039; border-radius: 4px; }
</style>
""", unsafe_allow_html=True)

# ── Sidebar ───────────────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown("### ⚙️ Settings")
    model_choice = st.selectbox(
        "Model",
        ["GPT-4.1 (OpenAI)", "Mistral Small 2506"],
        index=0,
    )
    st.markdown("---")
    if st.button("🗑️ Clear chat"):
        st.session_state.messages = []
        st.session_state.lc_messages = [SystemMessage(content="You're a funny AI agent")]
        st.rerun()

# ── Session state ─────────────────────────────────────────────────────────────
SYSTEM_PROMPT = "You're a funny AI agent"

if "messages" not in st.session_state:
    st.session_state.messages = []

if "lc_messages" not in st.session_state:
    st.session_state.lc_messages = [SystemMessage(content=SYSTEM_PROMPT)]

# ── LLM client ────────────────────────────────────────────────────────────────
@st.cache_resource
def get_client(choice: str):
    if choice.startswith("Mistral"):
        return ChatMistralAI(
            model="mistral-small-2506",
            temperature=0.2,
            max_tokens=512,
        )
    return ChatOpenAI(
        model="gpt-4.1",
        temperature=0.2,
    )

client = get_client(model_choice)

# ── Top info bar ──────────────────────────────────────────────────────────────
st.markdown(
    '<div class="top-bar">Type 0 to end the conversation (same as terminal version)</div>',
    unsafe_allow_html=True,
)

# ── Render messages ───────────────────────────────────────────────────────────
for msg in st.session_state.messages:
    if msg["role"] == "user":
        st.markdown(f"""
        <div class="msg-row">
            <div class="avatar avatar-user">🧑</div>
            <div class="msg-card">{msg["content"]}</div>
        </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown(f"""
        <div class="msg-row">
            <div class="avatar avatar-bot">🤖</div>
            <div class="msg-card">{msg["content"]}</div>
        </div>
        """, unsafe_allow_html=True)

# ── Chat input ────────────────────────────────────────────────────────────────
user_input = st.chat_input("Type your message...")

if user_input:
    if user_input.strip() == "0":
        st.markdown("""
        <div class="msg-row">
            <div class="avatar avatar-bot">🤖</div>
            <div class="msg-card">Goodbye! It was fun (mostly for me). 👋</div>
        </div>
        """, unsafe_allow_html=True)
        st.stop()

    st.session_state.messages.append({"role": "user", "content": user_input})
    st.session_state.lc_messages.append(HumanMessage(content=user_input))

    with st.spinner(""):
        response = client.invoke(st.session_state.lc_messages)

    bot_reply = response.content
    st.session_state.messages.append({"role": "assistant", "content": bot_reply})
    st.session_state.lc_messages.append(AIMessage(content=bot_reply))

    st.rerun()
