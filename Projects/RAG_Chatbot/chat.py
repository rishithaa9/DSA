import os
from dotenv import load_dotenv

from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains import create_retrieval_chain

load_dotenv()

api_key = os.getenv("GOOGLE_API_KEY")


def get_response(question):

    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    vectorstore = FAISS.load_local(
        "vectorstore",
        embeddings,
        allow_dangerous_deserialization=True
    )

    retriever = vectorstore.as_retriever(
        search_type="mmr",
        search_kwargs={
            "k": 4,
            "fetch_k": 10
        }
    )

    llm = ChatGoogleGenerativeAI(
        model="gemini-2.0-flash",
        google_api_key=api_key,
        temperature=0
    )

    prompt = ChatPromptTemplate.from_template("""
You are an AI assistant that answers questions using ONLY the provided document.

Rules:

1. Answer only from the context.
2. If the answer is not available, say:
   "I couldn't find the answer in the document."
3. Do not make assumptions.
4. Keep answers concise and accurate.

Context:
{context}

Question:
{input}
""")

    document_chain = create_stuff_documents_chain(llm, prompt)

    retrieval_chain = create_retrieval_chain(
        retriever,
        document_chain
    )

    response = retrieval_chain.invoke({"input": question})

    return response