import flare_python_periphery_package as fpp

from utils import get_provider

w3 = get_provider("coston2")

ftso_address = w3.to_checksum_address(fpp.name_to_address("FastUpdater", w3))
abi = fpp.coston2.abis.IFastUpdater
ftsov2 = w3.eth.contract(address=ftso_address, abi=abi)

feed_indexes = [0, 2, 9]
feeds, decimals, timestamp = ftsov2.functions.fetchCurrentFeeds(feed_indexes).call()

print("Feeds:", feeds)
print("Decimals:", decimals)
print("Timestamp:", timestamp)
