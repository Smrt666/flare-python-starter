import flare_python_periphery_package as fpp
from web3 import Web3

from utils import get_provider

w3 = get_provider("coston2")
WNat_address = Web3.to_checksum_address(fpp.name_to_address("WNat", w3))

print(f"WNat address: {WNat_address}")

WNat_contract = w3.eth.contract(WNat_address, abi=fpp.coston2.abis.IWNat)
symbol = WNat_contract.functions.symbol().call()

print(f"Symbol: {symbol}")
