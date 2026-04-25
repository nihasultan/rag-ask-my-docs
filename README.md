# 📄 Ask My Docs – Production RAG Application

An end-to-end Retrieval-Augmented Generation (RAG) system that allows users to query documents using natural language.

# Live Demo:
https://rag-ask-my-docs-8gntjzhca5cxug28eagp9m.streamlit.app/

# Overview

Ask My Docs is designed to solve a common problem:
How do you efficiently extract relevant information from large, unstructured documents?

This system allows users to:

-Ask natural language questions over PDFs
-Retrieve contextually relevant chunks
-Generate accurate, grounded answers using LLMs

# Key Features

🔍 Semantic Search over document content
⚡ Hybrid Retrieval using BM25 + FAISS
🎯 Cross-Encoder Reranking for improved relevance
📄 Multi-document Querying
💬 LLM-based Answer Generation with context grounding
🖥️ Interactive UI built with Streamlit

# System Architecture
The pipeline consists of the following stages:

1. Document Ingestion - PDF parsing and text extraction. Chunking into smaller, context-preserving segments.
2. Embedding & Indexing - Dense embeddings generated for each chunk and stored in FAISS for efficient vector search.
3. Hybrid Retrieval - BM25 for keyword-based retrieval and FAISS for semantic similarity search.
4. Reranking - Cross-Encoder model ranks retrieved chunks based on relevance.
5. Response Generation - Top-ranked chunks passed to LLM. Generates context-aware, grounded answers.

# Tech Stack
Language: Python
Retrieval: FAISS, BM25
LLM Integration: Groq API, local:tinyllama
Frontend: Streamlit

Setup Instructions
# Clone the repository
git clone https://github.com/nihasultan/<repo-name>.git

# Navigate to project directory
cd <repo-name>

# Install dependencies
pip install -r requirements.txt

# Run the application
streamlit run app.py