
import openai
import faiss
import numpy as np
import os

openai.api_key = os.getenv("OPENAI_API_KEY", "sk-...")

DIM = 1536
store = {"index": faiss.IndexFlatL2(DIM), "texts": [], "vectors": []}

def init_vector_store():
    return store

def embed_text(text):
    response = openai.Embedding.create(model="text-embedding-ada-002", input=text)
    return np.array(response["data"][0]["embedding"], dtype="float32")

def add_to_vector_store(store, text, chunk_size=500):
    chunks = [text[i:i+chunk_size] for i in range(0, len(text), chunk_size)]
    vectors = [embed_text(chunk) for chunk in chunks]
    store["index"].add(np.array(vectors))
    store["texts"].extend(chunks)
    store["vectors"].extend(vectors)

def query_vector_store(store, question, language="TH"):
    q_vector = embed_text(question)
    D, I = store["index"].search(np.array([q_vector]), k=3)
    context = "\n".join([store["texts"][i] for i in I[0] if i < len(store["texts"])])

    lang_prompt = {
        "TH": "คุณเป็นผู้ช่วยด้านกฎหมายประกันภัย ให้คำตอบเป็นภาษาไทยที่เข้าใจง่าย",
        "EN": "You are an insurance legal assistant. Answer in clear English."
    }

    prompt = f"""
{lang_prompt[language]}

Policy Excerpts:
"""
{context}
"""

Q: {question}
A:
"""
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt.strip()}]
        )
        return response["choices"][0]["message"]["content"].strip()
    except Exception as e:
        return f"[GPT Error: {str(e)}]"
