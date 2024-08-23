import asyncio

import flare_python_periphery_package as fpp
from web3 import AsyncWeb3

from utils import get_async_provider


async def main():
    w3 = await get_async_provider("coston2")
    WNat_address = await fpp.coston2.products.WNat.async_get_address(w3)

    print(f"WNat address: {WNat_address}")

    WNat_contract = w3.eth.contract(WNat_address, abi=fpp.coston2.products.WNat.abi)
    symbol = await WNat_contract.functions.symbol().call()

    print(f"Symbol: {symbol}")


if __name__ == "__main__":
    asyncio.run(main())
