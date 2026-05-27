import streamlit as st
import requests

st.set_page_config(page_title="Production RAG", page_icon="🔍", layout="wide")
st.title("🔍 Production RAG — Ask My Docs")
st.markdown("Enterprise-grade RAG with **Hybrid Search** + **Reranking** + **Citations**")

st.divider()

api_key = st.text_input("Enter your Groq API Key", type="password")

uploaded_file = st.file_uploader("Upload PDF Document", type="pdf")

if uploaded_file and st.button("📄 Process Document"):
    with st.spinner("Processing document with hybrid indexing..."):
        response = requests.post(
            "http://localhost:8000/upload",
            files={"file": (uploaded_file.name, uploaded_file, "application/pdf")}
        )
        if response.status_code == 200:
            st.success(response.json()["message"])
        else:
            st.error("Something went wrong!")

st.divider()

question = st.text_input("Ask a question about your document")

if question and api_key:
    if st.button("🔍 Ask"):
        with st.spinner("Retrieving → Reranking → Generating..."):
            response = requests.post(
                "https://production-rag-bf4k.onrender.com/analyze",
                data={"question": question, "api_key": api_key}
            )
            
            if response.status_code == 200:
                result = response.json()
                
                st.subheader("💬 Answer")
                st.markdown(result["answer"])
                
                st.divider()
                
                st.subheader("📚 Sources Used")
                for i, source in enumerate(result["sources"]):
                    with st.expander(f"Source {i+1}"):
                        st.write(source)
            else:
                st.error("Something went wrong!")