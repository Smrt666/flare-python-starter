import asyncio
from pprint import pprint

import flare_python_periphery_package as fpp

from utils import get_async_provider


async def main():
    w3 = await get_async_provider("coston2")

    # first get some c2flr on https://faucet.flare.network/coston2,
    # othervise this program might not work

    WNat_product = fpp.coston2.products.WNat
    WNat_contract = w3.eth.contract(
        await WNat_product.async_get_address(w3),
        abi=WNat_product.abi,
    )

    # send transaction
    tx_hash = await WNat_contract.functions.deposit().transact(
        {"value": w3.to_wei(1, "ether")}
    )
    # wait for receipt
    tx_receipt = await w3.eth.wait_for_transaction_receipt(tx_hash)

    pprint(tx_receipt)


if __name__ == "__main__":
    asyncio.run(main())
