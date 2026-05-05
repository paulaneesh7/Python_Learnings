import asyncio
import threading
import time

def background_worker():
    while True:
        time.sleep(1)
        print(f"Logging the system health 🕰️")



async def fetch_orders():
    await asyncio.sleep(3)
    print("🎁 order fetched")


t1 = threading.Thread(target=background_worker, daemon=True)

t1.start()

asyncio.run(fetch_orders())