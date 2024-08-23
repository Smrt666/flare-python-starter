import asyncio

from utils import get_async_provider


async def main():
    w3 = await get_async_provider("coston2")
    chain_id = await w3.eth.chain_id

    print(f"Chain ID: {chain_id}")


if __name__ == "__main__":
    asyncio.run(main())
