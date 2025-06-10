
import streamlit as st
import requests

st.set_page_config(page_title="🧾 Policy Summarizer", layout="centered")
st.title("🧾 Insurance Policy Q&A (RAG with GPT)")

uploaded_file = st.file_uploader("Upload Insurance Policy (PDF)", type=["pdf"])
language = st.radio("Language", ["TH", "EN"])
question = st.text_area("Your Question", "ค่ารักษาพยาบาล IPD มี deductible ไหม?")

if st.button("Ask"):
    if uploaded_file and question:
        with st.spinner("Processing..."):
            response = requests.post(
                "http://localhost:8000/summarize",
                files={"file": uploaded_file.getvalue()},
                data={"question": question, "language": language}
            )
            result = response.json()
            st.markdown(f"**Answer:** {result['answer']}")
    else:
        st.warning("Please upload a policy and enter a question.")
