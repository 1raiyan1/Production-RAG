from pypdf import PdfReader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.documents import Document
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import FakeEmbeddings
from rank_bm25 import BM25Okapi
import numpy as np

class HybridRetriever:
    def __init__(self):
        self.embeddings = FakeEmbeddings(size=384)
        self.vectorstore = None
        self.bm25 = None
        self.chunks = []

    def load_pdf(self, pdf_path):
        reader = PdfReader(pdf_path)
        text = ""
        for i, page in enumerate(reader.pages):
            text += f"\n[Page {i+1}]\n{page.extract_text()}"

        splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=100)
        self.chunks = splitter.split_text(text)

        docs = [Document(page_content=c, metadata={"chunk_id": i}) for i, c in enumerate(self.chunks)]
        self.vectorstore = FAISS.from_documents(docs, self.embeddings)

        tokenized = [c.split() for c in self.chunks]
        self.bm25 = BM25Okapi(tokenized)

    def retrieve(self, query, k=6):
        vector_results = self.vectorstore.similarity_search(query, k=k)
        vector_chunks = [r.page_content for r in vector_results]

        bm25_scores = self.bm25.get_scores(query.split())
        top_bm25_indices = np.argsort(bm25_scores)[::-1][:k]
        bm25_chunks = [self.chunks[i] for i in top_bm25_indices]

        combined = list(dict.fromkeys(vector_chunks + bm25_chunks))
        return combined[:k]