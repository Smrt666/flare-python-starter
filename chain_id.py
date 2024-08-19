from utils import get_provider

w3 = get_provider("coston2")
chain_id = w3.eth.chain_id

print(f"Chain ID: {chain_id}")
