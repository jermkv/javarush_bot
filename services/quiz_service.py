from openai import AsyncOpenAI
from config import OpenAI_KEY

client = AsyncOpenAI(api_key=OpenAI_KEY)


async def get_quiz_question(topic: str) -> str:
    response = await client.chat.completions.create(
        model='gpt-4',
        messages=[{
            'role': 'system', 'content': f'Сгенерируй один вопрос по теме {topic} и задай этот вопрос строго на русском языке.'
        }],
        temperature=0.7
    )
    return response.choices[0].message.content


async def check_answer(question: str, answer: str) -> str:
    response = await client.chat.completions.create(
        model="gpt-4",
        messages=[
            {
                "role": "system",
                "content": (
                    f"Проверь правильность ответа на квиз.\n"
                    f"Вопрос: {question}\n"
                    f"Ответ: {answer}\n"
                    'Скажи только одно слово: "правильно" или "неправильно".'
                ),
            }
        ],
        temperature=0,
    )
    print(response.choices[0].message.content.strip())
    return response.choices[0].message.content.strip()
