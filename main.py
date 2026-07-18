from telethon import TelegramClient, functions
import random
import string
import asyncio
import time

api_id = "39541901"      # Đã thay rồi thì giữ nguyên
api_hash = "d88151d38f1d4f740c89724ba66620e4"

client = TelegramClient('name_changer', api_id, api_hash)

emojis = ["🔥", "💀", "😈", "⚡", "🌟", "☠️", "🃏", "🐉", "🚀", "💎", "🩸", "❄️", "👑", "🔮", "⚔️"]

def generate_random_name():
    length = random.randint(8, 20)
    base = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length))
    
    if random.random() > 0.3:
        emoji1 = random.choice(emojis)
        emoji2 = random.choice(emojis) if random.random() > 0.5 else ""
        return f"{emoji1}{base}{emoji2}"
    return base

async def main():
    await client.start()
    print("🚀 Name Changer (Telethon) đang chạy...")

    while True:
        try:
            new_name = generate_random_name()
            await client(functions.account.UpdateProfileRequest(
                first_name=new_name
            ))
            print(f"[{time.strftime('%H:%M:%S')}] Đã đổi tên → {new_name}")
        except Exception as e:
            print(f"Lỗi: {e}")
        
        await asyncio.sleep(300)  # 30 phút = 1800 giây

if __name__ == "__main__":
    asyncio.run(main())
