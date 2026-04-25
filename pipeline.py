from generator import generate_answer
from ingestion import process_uploaded_file, load_and_process_pdfs
from retrieval import build_index, retrieve

chunks = None
index = None

def initialize(uploaded_file):
    global chunks, index

    file_path, file_name = process_uploaded_file(uploaded_file)

    chunks = load_and_process_pdfs(file_path, file_name)
    index, _ = build_index(chunks)

def ask(query):
    retrieved = retrieve(query, chunks, index)
    answer = generate_answer(query, retrieved)
    return answer, retrieved