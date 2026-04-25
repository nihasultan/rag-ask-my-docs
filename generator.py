from transformers import pipeline
import torch

generator = pipeline(
    "text-generation",          
    model="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    torch_dtype=torch.float16,  
    device_map=None         
)

def generate_answer(query, docs):
    context = "\n\n".join(
        [d.get("text", "")[:200] for d in docs[:3]]
    )

    messages = [
        {
            "role": "system",
            "content": "You are a helpful assistant. Answer questions using only the provided context. Write in complete sentences with bullet points. Do not repeat yourself."
        },
        {
            "role": "user",
            "content": f"Context:\n{context}\n\nQuestion: {query}"
        }
    ]

    prompt = generator.tokenizer.apply_chat_template(
        messages,
        tokenize=False,
        add_generation_prompt=True
    )

    result = generator(
        prompt,
        max_new_tokens=200,
        min_new_tokens=30,
        do_sample=False,
        repetition_penalty=1.3,
        no_repeat_ngram_size=4,
    )

    full_text = result[0]["generated_text"]
    answer = full_text[len(prompt):].strip()

    if answer and answer[-1] not in ".!?":
        last_period = max(answer.rfind("."), answer.rfind("!"), answer.rfind("?"))
        if last_period != -1:
            answer = answer[:last_period + 1]

    return answer