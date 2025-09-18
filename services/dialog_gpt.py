from openai import OpenAI
from config import OpenAI_KEY
client = OpenAI(api_key=OpenAI_KEY)


async def dialog_gpt_func(text):
    response = client.chat.completions.create(
        model='gpt-4o-mini',
        messages=[
            {'role': 'system', 'content': 'Ты интересный собеседник!'},
            {'role': 'user', 'content': text}
        ],
        temperature=0.7,
        max_tokens=400
    )

    return response.choices[0].message.content