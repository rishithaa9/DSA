import langchain
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains import create_retrieval_chain
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("GOOGLE_API_KEY")


def create_vectorstore(pdf_path):

    # Loading document
    loader = PyPDFLoader(pdf_path)
    documents = loader.load()

    print("Pages", len(documents))

    # print(type(documents))
    # print(type(documents[0]))
    # print(documents[0].page_content[:500])
    # print(documents[0].metadata) # it says in which page the content is present

    # converting the doc to chunks
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200
    )

    chunks = text_splitter.split_documents(documents)

    # print(len(chunks))
    # print(chunks[0])

    # Embeddings
    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    # Embed one chunk
    vector = embeddings.embed_query(chunks[0].page_content)

    # print(vector)
    # print(len(vector))

    # Creating Vectorstore(Database)
    vectorstore = FAISS.from_documents(chunks, embeddings)

    # create index.faiss,index.pkl
    vectorstore.save_local("vectorstore")

    print("Vectorstore created successfully!")

    return True