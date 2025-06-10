
# 🧾 AI Insurance Policy Summarizer (RAG + Multilingual + FAISS)

This tool processes insurance policy PDFs and uses a Retrieval-Augmented Generation (RAG) model to answer questions in Thai or English.

---

## 🧠 Features

- PDF OCR/Parsing
- FAISS vector store for long-term memory
- RAG pipeline with OpenAI GPT-4
- Thai and English language support
- Streamlit chatbot UI
- FastAPI backend

---

## 💻 How to Use

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Run Backend

```bash
uvicorn app.main:app --reload --port 8000
```

### 3. Run Streamlit Chatbot UI

```bash
streamlit run ui/chatbot.py
```

---

## ⚙️ Environment

Set your OpenAI key:

```bash
export OPENAI_API_KEY="your-openai-key"
```

---

## 🔐 Example Use Cases

- "What is the deductible for IPD?"
- "กรมธรรม์นี้คุ้มครองการคลอดบุตรไหม?"

Answer will be returned from the uploaded policy in Thai or English.
