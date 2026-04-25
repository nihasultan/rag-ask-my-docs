from transformers import pipeline

# Load once (cached by Streamlit automatically)
generator = pipeline(
    "text2text-generation",
    model="google/flan-t5-small",  # 🔥 small = fast + deployable
)

def generate_answer(query, docs):
    context = "\n\n".join([d.get("text", "") for d in docs])

    prompt = f"""
You are a strict formatting assistant.

RULES:
- Always respond in bullet points
- Each bullet must be a complete idea
- Do not write paragraphs
- Minimum 5 bullets

Context:
{context}

Question:
{query}

Answer in bullet points only:
"""

    result = generator(
        prompt,
        max_new_tokens=500,
        do_sample=False
    )

    return result[0]["generated_text"]