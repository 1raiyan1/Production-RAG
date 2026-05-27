from fastapi import FastAPI, UploadFile, File, Form
from app.retriever import HybridRetriever
from app.reranker import rerank
from app.generator import generate_answer
import shutil
import os

app = FastAPI()
retriever = HybridRetriever()

@app.post("/upload")
async def upload(file: UploadFile = File(...)):
    temp_path = f"temp_{file.filename}"
    with open(temp_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    
    retriever.load_pdf(temp_path)
    os.remove(temp_path)
    
    return {"message": f"Document loaded with {len(retriever.chunks)} chunks!"}

@app.post("/ask")
async def ask(question: str = Form(...), api_key: str = Form(...)):
    if not retriever.chunks:
        return {"error": "Please upload a document first!"}
    
    retrieved_chunks = retriever.retrieve(question, k=6)
    reranked_chunks = rerank(question, retrieved_chunks, api_key, top_k=4)
    answer = generate_answer(question, reranked_chunks, api_key)
    
    return {
        "answer": answer,
        "sources": reranked_chunks
    }