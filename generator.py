from transformers import pipeline

generator = pipeline(
    "text2text-generation",
    model="google/flan-t5-base",
)

def generate_answer(query, docs):
    context = "\n\n".join(
        [d.get("text", "")[:300] for d in docs[:3]]  
    )

    prompt = f"""Answer the question using the context below. List the key points separated by | character.

Context:
{context}

Question:
{query}

Key points separated by |:"""

result = generator(
    prompt,
    max_new_tokens=200,
    min_new_tokens=60,
    do_sample=False,
    no_repeat_ngram_size=3,
    early_stopping=False,
)

text = result[0]["generated_text"].strip()

# Split on the delimiter and format as bullet points
points = [p.strip() for p in text.split("|") if p.strip()]
bullet_output = "\n".join(f"• {p}" for p in points)
return bullet_output  