from openai import OpenAI
from config import OpenAI_KEY

client = OpenAI(api_key=OpenAI_KEY)

async def translate_text(text: str, target_lang: str) -> str:
    prompt = (
        f"Переведи следующий текст на {target_lang}:\n{text}\n"
        "Только перевод, без пояснений."
    )

    response = client.chat.completions.create(
        model='gpt-4o-mini',
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=0.2,
        max_tokens=512
    )

    return response.choices[0].message.content.strip()
