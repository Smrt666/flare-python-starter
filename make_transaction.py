from pprint import pprint

import flare_python_periphery_package as fpp

from utils import get_provider

w3 = get_provider("coston2")

# first get some c2flr on https://faucet.flare.network/coston2,
# othervise this program might not work

WNat_product = fpp.coston2.products.WNat
WNat_contract = w3.eth.contract(WNat_product.get_address(w3), abi=WNat_product.abi)

# send transaction
tx_hash = WNat_contract.functions.deposit().transact({"value": w3.to_wei(1, "ether")})
# wait for receipt
tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)

pprint(tx_receipt)
