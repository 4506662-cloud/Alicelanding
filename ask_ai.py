import os
from pathlib import Path
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv(Path(__file__).parent / ".env")

api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise RuntimeError("OPENAI_API_KEY не найден в .env")

client = OpenAI(api_key=api_key)

user_phrase = input("Введи фразу или мысль: ").strip()
if not user_phrase:
    user_phrase = "Я чувствую себя потерянным и не знаю, куда идти"

print("\nОтправляю запрос к OpenAI...\n")

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {
            "role": "system",
            "content": (
                "Ты — знаток книги Льюиса Кэрролла «Алиса в Стране Чудес». "
                "Когда пользователь пишет фразу или описывает своё состояние, ты:\n"
                "1. Даёшь краткую поэтичную трактовку этой фразы (2–3 предложения)\n"
                "2. Подбираешь подходящую цитату из книги и указываешь, кто её произнёс\n"
                "Отвечай по-русски, тон — мягкий и немного загадочный."
            ),
        },
        {"role": "user", "content": user_phrase},
    ],
    max_tokens=500,
)

print("=" * 60)
print(response.choices[0].message.content)
print("=" * 60)
