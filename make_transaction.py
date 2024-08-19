from pprint import pprint

import flare_python_periphery_package as fpp

from utils import get_provider

w3 = get_provider("coston2")

# first get some c2flr on https://faucet.flare.network/coston2,
# othervise this program might not work

WNat_contract = w3.eth.contract(
    w3.to_checksum_address(fpp.name_to_address("WNat", w3)), abi=fpp.coston2.abis.IWNat
)

# send transaction
tx_hash = WNat_contract.functions.deposit().transact({"value": w3.to_wei(1, "ether")})
# wait for receipt
tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)

pprint(tx_receipt)
