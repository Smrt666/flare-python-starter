import asyncio

import flare_python_periphery_package as fpp

from utils import get_async_provider


async def main():
    w3 = await get_async_provider("coston2")

    ftso_address = await fpp.coston2.products.FastUpdater.async_get_address(w3)
    abi = fpp.coston2.products.FastUpdater.abi

    # If you change chains a lot you might want to consider using something like this:
    # ftso_address = fpp.name_to_address("FastUpdater", w3)
    # abi = fpp.name_to_abi("FastUpdater", "coston2")

    ftsov2 = w3.eth.contract(address=ftso_address, abi=abi)

    feed_indexes = [0, 2, 9]
    feeds, decimals, timestamp = await ftsov2.functions.fetchCurrentFeeds(
        feed_indexes
    ).call()

    print("Feeds:", feeds)
    print("Decimals:", decimals)
    print("Timestamp:", timestamp)


if __name__ == "__main__":
    asyncio.run(main())
