
from fastapi import FastAPI, UploadFile, File, Form
from app.pdf_reader import extract_text_from_pdf
from app.vector_store import init_vector_store, add_to_vector_store, query_vector_store

app = FastAPI()
store = init_vector_store()

@app.post("/summarize")
async def summarize_policy(file: UploadFile = File(...), question: str = Form(...), language: str = Form("TH")):
    content = await file.read()
    extracted_text = extract_text_from_pdf(content)
    add_to_vector_store(store, extracted_text)
    response = query_vector_store(store, question, language)
    return {"question": question, "answer": response}
