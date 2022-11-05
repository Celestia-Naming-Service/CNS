import requests
import base64
from pprint import pprint


def get_data(namespace_id:str, height:int):
    r = requests.get(f'http://localhost:26658/namespaced_data/{namespace_id}/height/{height}')
    pprint(dict(r.json()))
    data = r.json()['data'][0]
    print(base64.b64decode(data).decode('utf-8'))
    return data

# get_data('756f60cbe7bf5401',32992)


n_id = '756f60cbe7bf5401'

def post_data(namespace_id, data, gas_limit=70000):
    data = data.encode('utf-8')
    d = data.hex()
    r = requests.post(f'http://localhost:26658/submit_pfd', json={"namespace_id":namespace_id,"data":d,"gas_limit":gas_limit})
    pprint(r.json()) 
    get_data('756f60cbe7bf5401',r.json()['height'])



post_data(n_id, "Yo World")