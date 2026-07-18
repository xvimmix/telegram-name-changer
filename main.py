from telethon import TelegramClient, functions
import random
import string
import asyncio
import time

api_id = "39541901"      # Đã thay rồi thì giữ nguyên
api_hash = "d88151d38f1d4f740c89724ba66620e4"

client = TelegramClient('name_changer', api_id, api_hash)

async def main():
    await client.start()
    print("🚀 Name Changer (Telethon) đang chạy...")

    while True:
        try:
            characters = string.ascii_letters + string.digits
            new_name = ''.join(random.choice(characters) for _ in range(10))
            
            await client(functions.account.UpdateProfileRequest(
                first_name=new_name
            ))
            print(f"[{time.strftime('%H:%M:%S')}] Đã đổi tên → {new_name}")
        except Exception as e:
            print(f"Lỗi: {e}")
        
        await asyncio.sleep(3600)  # 1 tiếng

if __name__ == "__main__":
    asyncio.run(main())
