import requests
from pprint import pprint

r = requests.get('https://dummyjson.com/products/1')

print(r.json())
'''
{'id': 1, 'title': 'iPhone 9', 'description': 'An apple': 4.69 ... 'thumbnail.jpg']}
'''

pprint(r.json())
'''
{'brand': 'Apple',
 'category': 'smartphones',
 'id': 1,
 'images': ['https://dummyjson.com/image/i/products/1/1.jpg',
            'https://dummyjson.com/image/i/products/1/2.jpg',
 'price': 549,
'''