import requests
from pprint import pprint

response = requests.get('http://127.0.0.1:8000/api/v1/articles/')
result = response.json()

pprint(result)