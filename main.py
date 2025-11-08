from telethon import TelegramClient
import asyncio

api_id = 1234567  # <-- твой api_id (число)
api_hash = 'YOUR_API_HASH'  # <-- твой api_hash (строка)
session_name = 'anon'       # имя сессии, можно не менять

# Пример структуры: города и их каналы-доноры
cities = {
    "samara": ["samarae1","samara_smi"]  # каналы из списка, которые ты мне присылал
}

async def main():
    client = TelegramClient(session_name, api_id, api_hash)
    await client.start()
    for city, channels in cities.items():
        for chan in channels:
            entity = await client.get_entity(chan)
            async for message in client.iter_messages(entity, limit=1):
                print(f"{city} — {chan}")
                print(f"ID: {message.id}, Дата: {message.date}")
                print(f"Текст: {message.text}")
                print("-" * 40)

if __name__ == "__main__":
    asyncio.run(main())
