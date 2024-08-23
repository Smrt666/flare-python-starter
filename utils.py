from dotenv import dotenv_values
from web3 import AsyncHTTPProvider, AsyncWeb3
from web3.middleware.geth_poa import async_geth_poa_middleware
from web3.middleware.signing import async_construct_sign_and_send_raw_middleware

env = dotenv_values(".env")


def get_rpc(chain: str) -> str:
    return {
        "coston": "https://coston2-api.flare.network/ext/C/rpc",
        "coston2": "https://coston2-api.flare.network/ext/C/rpc",
        "flare": "https://flare-api.flare.network/ext/C/rpc",
        "songbird": "https://songbird-api.flare.network/ext/C/rpc",
    }[chain]


async def get_async_provider(chain: str) -> AsyncWeb3:
    if chain in ("coston", "coston2"):
        # we need proof of authority for coston and coston2
        w3 = AsyncWeb3(
            AsyncHTTPProvider(get_rpc(chain)), middlewares=[async_geth_poa_middleware]
        )
    else:
        w3 = AsyncWeb3(AsyncHTTPProvider(get_rpc(chain)))

    private_key = env.get("ACCOUNT_PRIVATE_KEY", None)

    if not private_key:
        return w3

    account = w3.eth.account.from_key(private_key)
    # This middleware automatically captures transactions, signs them, and sends them as raw transactions.
    w3.eth.default_account = account.address
    w3.middleware_onion.add(await async_construct_sign_and_send_raw_middleware(account))

    return w3
