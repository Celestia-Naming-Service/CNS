# %%
import requests
import base64
from pprint import pprint

def get_data(namespace_id:str, height:int):
    r = requests.get(f'http://localhost:26659/namespaced_data/{namespace_id}/height/{height}')
    return dict(r.json())

# %%
def parse(data: str):
    decoded_data = base64.b64decode(data).decode('utf-8')
    return decoded_data

# %%
def post_data(namespace_id, data, gas_limit=70000):
    data = data.encode('utf-8')
    d = data.hex()
    r = requests.post(f'http://localhost:26659/submit_pfd', json={"namespace_id":namespace_id,"data":d,"gas_limit":gas_limit})
    pprint(r.json()) 
    print(get_data('756f60cbe7bf5401',r.json()['height']))

# %%
post_data('756f60cbe7bf5401', "{'Pratham': 'prasoon.cel'}")

# %%
# {"type": "REGISTER_NAME", "payload": {"name": "Pratham"}, signature: "123"}
state = dict() # initial state is empty

# TODO: real implementation
def get_address(signature):
    # pretend like the address is the signature
    return signature

# can be improved
def is_valid_address(address):
    return address == str

def update_state(action):
    actionType = action.get("type")
    address = get_address(action.get("signature"))
    if actionType == "REGISTER_NAME":
        name = action.get("payload").get("name")
        state.setdefault(name, address)
    elif actionType == "TRANSFER_NAME":
        name = action.get("payload").get("name")
        recipient = action.get("payload").get("recipient")
        if state.get(name) is address and is_valid_address(recipient):
            state.set(name, recipient)

# %% [markdown]
# #

# %% [markdown]
# # Historical Syncing
# We need to start from block 1 (or whatever block was the latest at the time that we launch this protocol) and process each block until the we get to the latest block.

# %%
my_namespace = '756f60cbe7bf5401'
initialHeight = 27070
latestHeight = 27525 # for example
for height in range(initialHeight, latestHeight):
    data_list = get_data(my_namespace, height)
    try:
        parsed_data = parse(data_list.get('data')[0])
        update_state(dict(eval(parsed_data)))
        print(dict(eval(parsed_data)))
        print(data_list)
    except Exception:
        pass


