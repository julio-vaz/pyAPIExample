from foxbit.utils import request
from foxbit.exceptions import InvalidOrderbookResponse


def get_orderbook(currency):
    endpoint = f'{currency}/orderbook?crypto_currency=BTC'
    response = request('get', endpoint)
    if response.status_code == 200:
        return response.json()
    else:
        raise InvalidOrderbookResponse()
