from groq import Groq
import streamlit as st

client = Groq(api_key=st.secrets["GROQ_API_KEY"])

def generate_answer(query, docs):

    context = "\n\n".join(
        [d.get("text", "")[:500] for d in docs[:4]]
    )

    prompt = f"""
You are a helpful AI assistant.

Answer ONLY using the context below.

Write:
- Clear bullet points
- Full sentences
- Structured answer

Context:
{context}

Question:
{query}

Answer:
"""

    response = client.chat.completions.create(
        model="llama3-8b-8192",
        messages=[
            {"role": "system", "content": "You are a precise assistant."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.3,
        max_tokens=600
    )

    return response.choices[0].message.content