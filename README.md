# Flare Python Starter
Rewrite of tutorial on [https://dev.flare.network/network/guides/flare-for-python-developers/#make-query](https://dev.flare.network/network/guides/flare-for-python-developers/#make-query) using flare python periphery library,

## Getting started
First clone and intsall dependencies:
```bash
git clone https://github.com/Smrt666/flare-python-starter.git
cd flare-python-starter
```
If you want to, now is the time to create python [virtual environment](https://docs.python.org/3/library/venv.html#how-venvs-work).
After that install dependencies (todo: flare-python-periphery-package):
```bash
pip install --index-url https://test.pypi.org/simple/ flare-python-periphery-package --extra-index-url https://pypi.org/simple poirot
pip install web3 python-dotenv
```

After that you can try:
* chain_id.py
* get_abi.py
* make_query.py
* check how utils.py work
* create_account.py, copy env.example into .env and set ACCOUNT and ACCOUNT_PRIVATE_KEY
* get some free c2flr on https://faucet.flare.network/coston2
* make_transaction.py
