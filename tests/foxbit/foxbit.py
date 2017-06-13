from foxbit import utils
from foxbit import foxbit
from foxbit import exceptions
import responses
import pytest


def register_orderbook_success_response():
    url = utils.build_url('BRL/orderbook?crypto_currency=BTC')
    response_body = {
        'pair': 'BTCBRL2',
        'bids': [
            [
                9680,
                0.09986983,
                90938008
            ],
        ],
    }
    responses.add(responses.GET, url, json=response_body,
                  status=200, match_querystring=True)


def register_orderbook_failure_response():
    url = utils.build_url('BRL/orderbook?crypto_currency=BTC')
    responses.add(responses.GET, url, status=500, match_querystring=True)


@responses.activate
def test_get_orderbook_success():
    register_orderbook_success_response()
    orderbook = foxbit.get_orderbook('BRL')
    print(orderbook)
    assert orderbook['pair'] == 'BTCBRL2'


@responses.activate
def test_get_orderbook_failure():
    register_orderbook_failure_response()
    with pytest.raises(exceptions.InvalidOrderbookResponse):
        foxbit.get_orderbook('BRL')
