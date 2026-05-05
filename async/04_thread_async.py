import asyncio
import time
from concurrent.futures import ThreadPoolExecutor




def check_stock(item):
    print(f"Check {item} in store...")
    time.sleep(2) #blocking operations
    return f"{item} stock: 42"


async def main():
    loop = asyncio.get_running_loop()
    with ThreadPoolExecutor() as pool:
        result = await loop.run_in_executor(pool, check_stock, "Masala Chai")
        print(result)

asyncio.run(main())