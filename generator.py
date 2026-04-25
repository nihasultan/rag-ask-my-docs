from groq import Groq
import streamlit as st

client = Groq(api_key=st.secrets["GROQ_API_KEY"])

def generate_answer(query, docs):

    context = "\n\n".join(
    [d.get("text", "")[:300] for d in docs[:3]]
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

    try:
        response = client.chat.completions.create(
            model="llama3-8b-8192",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.3,
            max_tokens=400
        )
        return response.choices[0].message.content

    except Exception as e:
        return f"❌ GROQ ERROR: {repr(e)}"