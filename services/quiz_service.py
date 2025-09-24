from openai import AsyncOpenAI
from config import OpenAI_KEY

client = AsyncOpenAI(api_key=OpenAI_KEY)


async def get_quiz_question(topic: str) -> str:
    prompt = f'Сгенерируй новый простой вопрос по теме {topic}, на который можно было бы дать ответ однозначный, фактический. '

    print(prompt)

    response = await client.chat.completions.create(
        model='gpt-4o-mini',
        messages=[{
            'role': 'system', 'content': prompt
        }],
        temperature=0.7
    )

    print(response)
    return response.choices[0].message.content


async def check_answer(question: str, answer: str) -> str:
    prompt = (
        f"Проверь правильность ответа на квиз.\n"
        f"Вопрос: {question}\n"
        f"Ответ: {answer}\n"
        f'Скажи "правильно" или "неправильно". Дай краткое объяснение.'
    )


    response = await client.chat.completions.create(
        model='gpt-4o-mini',
        messages=[
            {'role': 'system', 'content': prompt}
        ],
        temperature=0.7
    )

    print(response)

    return response.choices[0].message.content.strip().lower()