import os
import requests
import streamlit as st

API_URL = "https://api-inference.huggingface.co/models/google/flan-t5-large"
HEADERS = {
    "Authorization": f"Bearer {st.secrets['HUGGINGFACE_API_KEY']}"
}

def query_hf(payload):
    response = requests.post(API_URL, headers=HEADERS, json=payload)

    # debug info
    if response.status_code != 200:
        print("HF ERROR:", response.status_code, response.text)
        return {"error": response.text}

    try:
        return response.json()
    except:
        print("Non-JSON response:", response.text)
        return {"error": "Invalid response from HF"}

def generate_answer(query, docs):
    context = "\n\n".join([d.get("text", "") for d in docs])

    prompt = f"""
Answer the question in detail using the context below.

Give at least 5 bullet points.

Context:
{context}

Question:
{query}

Answer:
"""

    output = query_hf({
        "inputs": prompt,
        "parameters": {
            "max_new_tokens": 500,
            "temperature": 0.3
        }
    })
    if isinstance(output, dict) and "error" in output:
    return "Model is loading or API error. Please try again in a few seconds."

    try:
        return output[0]["generated_text"]
    except:
        return "Error generating answer. Try again."