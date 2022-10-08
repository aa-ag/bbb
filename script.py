import requests

url = 'https://api.bbb.org/token'
headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
    }
r = requests.post(
        url,
        headers=headers
    )