from sanic.response import json
from pyAPIExample import app
from foxbit import get_orderbook


@app.get("/orderbook")
async def orderbook(request):
    orderbook = get_orderbook('BRL')
    return json(orderbook)
