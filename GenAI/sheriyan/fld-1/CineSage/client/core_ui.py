import os
import json
from dotenv import load_dotenv
import streamlit as st
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel
from typing import List, Optional

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# ── Page config ───────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="Movie Information Extractor",
    page_icon="🎬",
    layout="centered",
)

# ── Custom CSS ────────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Fira+Code:wght@400;500&display=swap');

html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
    background-color: #0e0e0e;
    color: #e8e8e8;
}

#MainMenu, footer, header { visibility: hidden; }
.block-container {
    padding-top: 2.5rem;
    padding-bottom: 3rem;
    max-width: 900px;
}

/* ── Title ── */
.page-title {
    font-size: 2.8rem;
    font-weight: 700;
    color: #ffffff;
    margin-bottom: 1.8rem;
}

/* ── Label ── */
.input-label {
    font-size: 0.9rem;
    color: #aaaaaa;
    margin-bottom: 0.4rem;
}

/* ── Textarea ── */
textarea {
    background-color: #1a1a1a !important;
    color: #e8e8e8 !important;
    border: 1.5px solid #333 !important;
    border-radius: 8px !important;
    font-family: 'Inter', sans-serif !important;
    font-size: 1rem !important;
    line-height: 1.7 !important;
    padding: 1rem 1.2rem !important;
    caret-color: #fff;
}
textarea:focus {
    border-color: #cc2222 !important;
    box-shadow: 0 0 0 2px rgba(200,30,30,0.2) !important;
}

/* ── Button ── */
div.stButton > button {
    background: transparent !important;
    color: #e8e8e8 !important;
    border: 1.5px solid #555 !important;
    border-radius: 6px !important;
    font-size: 0.95rem !important;
    font-weight: 500 !important;
    padding: 0.55rem 1.6rem !important;
    margin-top: 0.6rem;
    transition: border-color 0.2s, color 0.2s;
}
div.stButton > button:hover {
    border-color: #aaa !important;
    color: #fff !important;
}

/* ── Section headers ── */
.section-title {
    font-size: 1.6rem;
    font-weight: 700;
    color: #ffffff;
    margin: 2rem 0 1rem 0;
}

/* ── 1. Structured field rows ── */
.result-section { margin-top: 0.5rem; }
.result-row {
    display: flex;
    gap: 0.6rem;
    padding: 0.55rem 0;
    border-bottom: 1px solid #1e1e1e;
    font-size: 1rem;
    line-height: 1.6;
}
.result-label { color: #888; min-width: 160px; font-weight: 500; }
.result-value { color: #e0e0e0; }

/* ── 2. Raw JSON code block ── */
.raw-block {
    background: #141414;
    border: 1px solid #2a2a2a;
    border-radius: 10px;
    padding: 1.4rem 1.6rem;
    font-family: 'Fira Code', monospace;
    font-size: 0.88rem;
    line-height: 1.85;
    overflow-x: auto;
    white-space: pre;
}
.json-brace   { color: #e0e0e0; }
.json-key     { color: #4ec9b0; }
.json-str     { color: #ce9178; }
.json-num     { color: #b5cea8; }
.json-bool    { color: #569cd6; }
.json-null    { color: #569cd6; }
.json-bracket { color: #e0e0e0; }

/* ── 3. JSON tree ── */
.tree-block {
    background: #141414;
    border: 1px solid #2a2a2a;
    border-radius: 10px;
    padding: 1.4rem 1.6rem;
    font-family: 'Fira Code', monospace;
    font-size: 0.88rem;
    line-height: 2;
}
.tree-key     { color: #4ec9b0; }
.tree-str     { color: #ce9178; }
.tree-num     { color: #b5cea8; }
.tree-bracket { color: #e0e0e0; }
.tree-index   { color: #888; }
.tree-indent  { margin-left: 1.6rem; }

hr { border: none; border-top: 1px solid #1e1e1e; margin: 1.5rem 0; }

::-webkit-scrollbar { width: 4px; }
::-webkit-scrollbar-track { background: #0e0e0e; }
::-webkit-scrollbar-thumb { background: #333; border-radius: 4px; }
</style>
""", unsafe_allow_html=True)

# ── Pydantic model ────────────────────────────────────────────────────────────
class Movie(BaseModel):
    title: str
    release_year: Optional[int] = None
    genre: List[str] = []
    director: Optional[str] = None
    cast: List[str] = []
    rating: Optional[float] = None
    awards: Optional[List[str]] = None
    summary: str

# ── Helpers ───────────────────────────────────────────────────────────────────
def syntax_highlight_json(raw: str) -> str:
    """Colorize a raw JSON string with span tags."""
    import re
    raw = raw.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

    def colorize(match):
        token = match.group(0)
        if token.startswith('"'):
            # key or string value — detect by trailing colon
            if re.match(r'"[^"]*"\s*:', token):
                key, rest = re.match(r'(".*?")(\s*:)', token).groups()
                return f'<span class="json-key">{key}</span>{rest}'
            return f'<span class="json-str">{token}</span>'
        if re.match(r'^-?\d+(\.\d+)?$', token):
            return f'<span class="json-num">{token}</span>'
        if token in ('true', 'false'):
            return f'<span class="json-bool">{token}</span>'
        if token == 'null':
            return f'<span class="json-null">{token}</span>'
        return token

    pattern = r'"(?:\\.|[^"\\])*"\s*:|"(?:\\.|[^"\\])*"|-?\d+(?:\.\d+)?|true|false|null'
    return re.sub(pattern, colorize, raw)


def render_tree(obj, indent=0) -> str:
    """Recursively render a JSON object as an HTML tree like a JSON viewer."""
    pad = '<span class="tree-indent">' * indent + '</span>' * indent
    inner_pad = '<span class="tree-indent">' * (indent + 1) + '</span>' * (indent + 1)
    html = ""

    if isinstance(obj, dict):
        html += f'<span class="tree-bracket">{{</span><br>'
        for k, v in obj.items():
            html += f'{inner_pad}<span class="tree-key">"{k}"</span> : '
            if isinstance(v, (dict, list)):
                html += render_tree(v, indent + 1)
            elif isinstance(v, str):
                html += f'<span class="tree-str">"{v}"</span><br>'
            elif v is None:
                html += f'<span class="json-null">null</span><br>'
            else:
                html += f'<span class="tree-num">{v}</span><br>'
        html += f'{pad}<span class="tree-bracket">}}</span><br>'

    elif isinstance(obj, list):
        html += f'<span class="tree-bracket">[</span><br>'
        for i, item in enumerate(obj):
            html += f'{inner_pad}<span class="tree-index">{i}</span> : '
            if isinstance(item, (dict, list)):
                html += render_tree(item, indent + 1)
            elif isinstance(item, str):
                html += f'<span class="tree-str">"{item}"</span><br>'
            else:
                html += f'<span class="tree-num">{item}</span><br>'
        html += f'{pad}<span class="tree-bracket">]</span><br>'

    return html


# ── LLM & Prompt ─────────────────────────────────────────────────────────────
@st.cache_resource
def get_client():
    return ChatOpenAI(model="gpt-4.1", temperature=0.2)

parser = PydanticOutputParser(pydantic_object=Movie)
client = get_client()

extraction_prompt = ChatPromptTemplate.from_messages([
    ("system", """
    Extract movie information from the paragraph
    {format_instructions}
"""),
    ("human", "{paragraph}")
])

# ── UI ────────────────────────────────────────────────────────────────────────
st.markdown('<div class="page-title">🎬 Movie Information Extractor</div>', unsafe_allow_html=True)
st.markdown('<div class="input-label">Enter movie paragraph:</div>', unsafe_allow_html=True)

para = st.text_area(
    label="",
    placeholder="Paste your movie paragraph here...",
    height=220,
    label_visibility="collapsed",
)

if st.button("Extract Information"):
    if para.strip():
        with st.spinner("Extracting..."):
            FINAL_PROMPT = extraction_prompt.invoke({
                "paragraph": para,
                "format_instructions": parser.get_format_instructions()
            })
            response = client.invoke(FINAL_PROMPT)
            raw_output = response.content
            movie: Movie = parser.parse(raw_output)
            movie_dict = json.loads(movie.model_dump_json())

        # ── Section 1: Clean field rows ───────────────────────────────────────
        st.markdown('<div class="section-title">📋 Extracted Information</div>', unsafe_allow_html=True)

        fields = {
            "Movie Title":   movie.title,
            "Release Year":  str(movie.release_year) if movie.release_year else "Not mentioned",
            "Genre":         ", ".join(movie.genre) if movie.genre else "Not mentioned",
            "Director":      movie.director or "Not mentioned",
            "Main Cast":     ", ".join(movie.cast) if movie.cast else "Not mentioned",
            "Rating":        str(movie.rating) if movie.rating else "Not mentioned",
            "Awards":        ", ".join(movie.awards) if movie.awards else "Not mentioned",
            "Short Summary": movie.summary,
        }

        rows_html = '<div class="result-section">'
        for label, value in fields.items():
            rows_html += f"""
            <div class="result-row">
                <div class="result-label">{label}:</div>
                <div class="result-value">{value}</div>
            </div>"""
        rows_html += "</div>"
        st.markdown(rows_html, unsafe_allow_html=True)

        st.markdown("<hr>", unsafe_allow_html=True)

        # ── Section 2: Raw Model Output ───────────────────────────────────────
        st.markdown('<div class="section-title">🖥️ Raw Model Output</div>', unsafe_allow_html=True)

        pretty_raw = raw_output.strip()
        highlighted = syntax_highlight_json(pretty_raw)
        st.markdown(
            f'<div class="raw-block">{highlighted}</div>',
            unsafe_allow_html=True,
        )

        st.markdown("<hr>", unsafe_allow_html=True)

        # ── Section 3: Structured Output (JSON tree) ──────────────────────────
        st.markdown('<div class="section-title">🌳 Structured Output</div>', unsafe_allow_html=True)

        tree_html = f'<div class="tree-block">{render_tree(movie_dict)}</div>'
        st.markdown(tree_html, unsafe_allow_html=True)

    else:
        st.warning("Please enter a paragraph first.")