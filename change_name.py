import asyncio
import random
import string
from pyrogram import Client
from datetime import datetime

api_id = "39541901"
api_hash = "d88151d38f1d4f740c89724ba66620e4"

interval_minutes = 60
name_length = 10

app = Client("name_changer", api_id, api_hash)

def generate_random_name():
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(name_length))

async def change_name():
    while True:
        try:
            new_name = generate_random_name()
            await app.update_profile(first_name=new_name)
            print(f"[{datetime.now().strftime('%H:%M:%S')}] Đã đổi tên → {new_name}")
        except Exception as e:
            print(f"Lỗi: {e}")
        await asyncio.sleep(interval_minutes * 60)

async def main():
    await app.start()
    print("🚀 Name Changer đang chạy trên Railway...")
    await change_name()

if __name__ == "__main__":
    asyncio.run(main())