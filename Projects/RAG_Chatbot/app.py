import streamlit as st
import os

from ingest import create_vectorstore
from chat import get_response

st.set_page_config(
    page_title="AI PDF Chatbot",
    page_icon="📄",
    layout="wide"
)

st.title("📄 AI PDF Chatbot")
st.write("Ask questions from your PDF using Gemini + LangChain + FAISS")

# -----------------------
# Session State
# -----------------------

if "messages" not in st.session_state:
    st.session_state.messages = []

# -----------------------
# Sidebar
# -----------------------

with st.sidebar:

    st.header("Upload PDF")

    uploaded_file = st.file_uploader(
        "Choose a PDF",
        type="pdf"
    )

    if uploaded_file:

        if not os.path.exists("data"):
            os.makedirs("data")

        pdf_path = os.path.join(
            "data",
            uploaded_file.name
        )

        with open(pdf_path, "wb") as f:
            f.write(uploaded_file.getbuffer())

        if st.button("Process PDF"):

            with st.spinner("Creating Vector Database..."):

                create_vectorstore(pdf_path)

            st.success("PDF processed successfully!")

# -----------------------
# Display Chat
# -----------------------

for message in st.session_state.messages:

    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# -----------------------
# User Input
# -----------------------

question = st.chat_input("Ask a question")

if question:

    st.session_state.messages.append(
        {
            "role":"user",
            "content":question
        }
    )

    with st.chat_message("user"):
        st.markdown(question)

    with st.spinner("Thinking..."):

        response = get_response(question)

        answer = response["answer"]

        sources = []

        for doc in response["context"]:
            page = doc.metadata.get("page",0)+1

            if page not in sources:
                sources.append(page)

        final_answer = answer

        if sources:

            final_answer += "\n\n### 📚 Source Pages\n"

            for page in sources:
                final_answer += f"- Page {page}\n"

    with st.chat_message("assistant"):
        st.markdown(final_answer)

    st.session_state.messages.append(
        {
            "role":"assistant",
            "content":final_answer
        }
    )