import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000/verify"

st.set_page_config(page_title="AI Answer Verification System")

st.title("AI Answer Verification System")
st.write("Verify AI-generated answers using RAG and secondary sources.")

question = st.text_area(
    "Enter your question",
    placeholder="e.g. What is artificial intelligence?"
)

if st.button("Verify Answer"):
    if not question.strip():
        st.warning("Please enter a question.")
    else:
        with st.spinner("Verifying..."):
            response = requests.post(
                API_URL,
                json={"question": question}
            )

        if response.status_code == 200:
            data = response.json()

            st.subheader("RAG Answer")
            st.write(data["rag_answer"])

            st.subheader("Web Answer")
            st.write(data["web_answer"])

            st.subheader("Verdict")
            st.success(f'{data["verdict"]} (Confidence: {data["confidence"]})')

            st.subheader("Explanation")
            st.write(data["explanation"])
        else:
            st.error("Failed to get response from backend.")
