import requests

output = requests.post('http://localhost:26658/submit_pfd', data = {"namespace_id": "0c204d39600fddd3", "data": "f1f20ca8007e910a3bf8b2e61da0f26bca07ef78717a6ea54165f5", "gas_limit": '70000'})
print(output.json())