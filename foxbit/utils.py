import requests

FOXBIT_API_URL = 'https://api.blinktrade.com/api/v1'


def request(method, endpoint, **kwargs):
    url = build_url(endpoint)
    return requests.request(method, url, verify=False, **kwargs)


def build_url(endpoint):
    return f'{FOXBIT_API_URL}/{endpoint}'
