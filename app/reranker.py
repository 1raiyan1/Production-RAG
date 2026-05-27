from groq import Groq

def rerank(query, chunks, api_key, top_k=4):
    client = Groq(api_key=api_key)
    
    chunks_text = ""
    for i, chunk in enumerate(chunks):
        chunks_text += f"\n[Chunk {i+1}]\n{chunk}\n"
    
    prompt = f"""You are a relevance judge. Given a query and chunks of text, rank the chunks by relevance to the query.

Query: {query}

Chunks:
{chunks_text}

Return ONLY the chunk numbers in order of relevance (most relevant first), like: 3,1,5,2
Just the numbers, nothing else."""

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "user", "content": prompt}]
    )
    
    ranking = response.choices[0].message.content.strip()
    
    try:
        indices = [int(x.strip())-1 for x in ranking.split(",")]
        reranked = [chunks[i] for i in indices if i < len(chunks)]
        return reranked[:top_k]
    except:
        return chunks[:top_k]