from telethon import TelegramClient, functions
import random
import string
import asyncio
import time

api_id = "39541901"      # Đã thay rồi thì giữ nguyên
api_hash = "d88151d38f1d4f740c89724ba66620e4"

client = TelegramClient('name_changer', api_id, api_hash)

emojis = ["🔥","💀","😈","⚡","🌟","☠️","🃏","🐉","🚀","💎","🩸","❄️","👑","🔮","⚔️","🪩","🎃","🕹️","☢️","🌀","🌈"]

change_count = 0

def generate_random_name():
    # Cố định 10 ký tự
    base = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(10))
    
    emoji1 = random.choice(emojis)
    emoji2 = random.choice(emojis)
    
    # Format: emoji1 + base + emoji2
    return f"{emoji1}{base}{emoji2}"

async def main():
    global change_count
    await client.start()
    print("🚀 Name Changer đang chạy (5 phút/lần)...")

    while True:
        try:
            new_name = generate_random_name()
            await client(functions.account.UpdateProfileRequest(
                first_name=new_name
            ))
            change_count += 1
            print(f"[{time.strftime('%H:%M:%S')}] ✅ Đã đổi → {new_name} | Lần: {change_count}")
        except Exception as e:
            print(f"[{time.strftime('%H:%M:%S')}] ❌ Lỗi: {e}")
        
        await asyncio.sleep(300)  # 5 phút

if __name__ == "__main__":
    asyncio.run(main())
