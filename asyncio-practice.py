import asyncio

async def make_americano():
    await asyncio.sleep(3)
    return "AMERICANO"

async def make_latte():
    await asyncio.sleep(3)
    return "LATTE"

async def main():
    coro1 = make_americano()
    coro2 = make_latte()
    result = await asyncio.gather(
        coro1,
        coro2
    )
    print(result)

asyncio.run(main())