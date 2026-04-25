from generator import generate_answer
from ingestion import load_and_process_pdfs
from retrieval import build_index, retrieve

chunks = None
index = None

def initialize():
    global chunks, index
    chunks = load_and_process_pdfs()
    index, _ = build_index(chunks)

def ask(query):
    retrieved = retrieve(query, chunks, index)
    answer = generate_answer(query, retrieved)
    return answer, retrieved