from openai import OpenAI
from config import OpenAI_KEY

client = OpenAI(api_key=OpenAI_KEY)

async def get_recommendations(rec_type: str, genre: str, not_liked: list) -> str:
    prompt = f"Посоветуй {rec_type} в жанре {genre}. Only ONE item at time!"
    if not_liked:
        prompt += f" Не предлагай: {', '.join(not_liked)}."
    prompt += " Только название и краткое описание."
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7,
        max_tokens=512
    )
    return response.choices[0].message.content.strip()
