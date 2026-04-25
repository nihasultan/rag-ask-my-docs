from transformers import pipeline

generator = pipeline(
    "text2text-generation",
    model="google/flan-t5-base",
)

def generate_answer(query, docs):
    \
    context = "\n\n".join(
        [d.get("text", "")[:150] for d in docs[:3]] 
    )

    prompt = f"""Write a fluent paragraph answering the question. Do not use bullet points or lists. Write complete sentences only.

Context:
{context}

Question:
{query}

Answer in one complete paragraph:"""

    result = generator(
        prompt,
        max_new_tokens=200,        
        min_new_tokens=60,
        do_sample=False,
        no_repeat_ngram_size=3,
        early_stopping=False,      
    )

    text = result[0]["generated_text"].strip()

    if text and not text[-1] in ".!?":
        last_period = max(text.rfind("."), text.rfind("!"), text.rfind("?"))
        if last_period != -1:
            text = text[:last_period + 1]

    return text