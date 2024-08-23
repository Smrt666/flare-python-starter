from web3 import AsyncWeb3

w3 = AsyncWeb3()
acc = w3.eth.account.create()
print(f"Account: {acc.address}, Private Key: {w3.to_hex(acc.key)}")
