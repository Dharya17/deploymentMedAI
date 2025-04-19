from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import faiss
import numpy as np

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Adjust for production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Query(BaseModel):
    text: str

@app.get("/")
def read_root():
    return {"message": "Backend is running"}

@app.post("/query")
def handle_query(query: Query):
    # Dummy FAISS index and example logic
    dim = 512
    index = faiss.IndexFlatL2(dim)
    sample_vector = np.random.rand(1, dim).astype("float32")
    index.add(sample_vector)
    
    query_vector = np.random.rand(1, dim).astype("float32")
    D, I = index.search(query_vector, 1)

    return {
        "result": f"Closest index: {I[0][0]} with distance: {D[0][0]}"
    }
