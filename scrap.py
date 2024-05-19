from requests import Request, Session
import json


url = 'https://pro-api.coinmarketcap.com/v2/cryptocurrency/quotes/latest'


def information(var):
    parameters = {
        'slug':var,
        'convert':'USD'        
    }

    headers = {
        'Accepts':'application/json',
        'X-CMC_PRO_API_KEY':'e6522703-0d67-4d98-8c3b-82e0ad2a4976'
    }

    session = Session()
    session.headers.update(headers)

    response = session.get(url, params = parameters)
    return json.loads(response.text)['data'][Dict[var]]['quote']['USD']['price']


Dict = {'bitcoin':'1', 'ethereum':'1027',
        'tether':'825', 'bnb':'1839', 'dogecoin':'74',
        'solana':'5426', 'maker':'1518'}
