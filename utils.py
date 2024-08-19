from dotenv import dotenv_values
from web3 import HTTPProvider, Web3
from web3.middleware.geth_poa import geth_poa_middleware
from web3.middleware.signing import construct_sign_and_send_raw_middleware

env = dotenv_values(".env")


def get_rpc(chain: str) -> str:
    return {
        "coston": "https://coston2-api.flare.network/ext/C/rpc",
        "coston2": "https://coston2-api.flare.network/ext/C/rpc",
        "flare": "https://flare-api.flare.network/ext/C/rpc",
        "songbird": "https://songbird-api.flare.network/ext/C/rpc",
    }[chain]


def get_provider(chain: str) -> Web3:
    w3 = Web3(HTTPProvider(get_rpc(chain)), middlewares=[geth_poa_middleware])

    private_key = env.get("ACCOUNT_PRIVATE_KEY", None)

    if not private_key:
        return w3

    account = w3.eth.account.from_key(private_key)
    # This middleware automatically captures transactions, signs them, and sends them as raw transactions.
    w3.eth.default_account = account.address
    w3.middleware_onion.add(construct_sign_and_send_raw_middleware(account))

    return w3
