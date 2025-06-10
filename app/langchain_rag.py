
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Qdrant
from langchain.llms import OpenAI
from langchain.chains import RetrievalQA
import os
import qdrant_client

openai_api_key = os.getenv("OPENAI_API_KEY", "sk-...")
qdrant_url = os.getenv("QDRANT_URL", "http://localhost:6333")

client = qdrant_client.QdrantClient(url=qdrant_url)
embeddings = OpenAIEmbeddings(openai_api_key=openai_api_key)
llm = OpenAI(openai_api_key=openai_api_key)

qa_chain = None

def setup_qdrant_rag(collection_name="policies", texts=[]):
    global qa_chain
    qdrant = Qdrant.from_texts(texts, embeddings, collection_name=collection_name, client=client)
    retriever = qdrant.as_retriever()
    qa_chain = RetrievalQA.from_chain_type(llm=llm, retriever=retriever)

def query_qdrant_rag(question):
    if qa_chain is None:
        return "Knowledge base not initialized."
    return qa_chain.run(question)
