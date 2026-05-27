from groq import Groq

def generate_answer(query, chunks, api_key):
    client = Groq(api_key=api_key)
    
    context = ""
    for i, chunk in enumerate(chunks):
        context += f"\n[Source {i+1}]\n{chunk}\n"
    
    prompt = f"""You are a helpful assistant. Answer the question based ONLY on the provided sources below.

IMPORTANT RULES:
- You MUST cite sources using [Source X] format
- If the answer is not in the sources, say "I cannot find this information in the provided documents"
- Be specific and accurate
- Never make up information

Sources:
{context}

Question: {query}

Answer (with citations):"""

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "user", "content": prompt}]
    )
    
    return response.choices[0].message.content