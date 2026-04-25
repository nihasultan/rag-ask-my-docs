from transformers import pipeline

generator = pipeline(
    "text2text-generation",
    model="google/flan-t5-base",  
)

def generate_answer(query, docs):
    context = "\n\n".join([d.get("text", "") for d in docs])

    prompt = f"""
You are an expert assistant.

Your job is to answer the question using ONLY the context below.

Write a detailed answer using bullet points.

Each bullet should contain real information from the context.

Context:
{context}

Question:
{query}

Answer:
"""

    result = generator(
        prompt,
        max_new_tokens=500,
        do_sample=False
    )

    return result[0]["generated_text"]