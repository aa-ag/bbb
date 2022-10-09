import requests
from dotenv import load_dotenv
import os
import json

load_dotenv()

bbbUSERNAME = os.environ["bbbUSERNAME"]
bbbPASSWORD = os.environ["bbbPASSWORD"]

url = 'https://api.bbb.org/token'

headers = {
        'content-Type': 'application/x-www-form-urlencoded'
    }

request_body = "grant_type=password&username={0}&password={1}".format(
    bbbUSERNAME, bbbPASSWORD
)

request_body = json.dumps(request_body)
print(request_body)

r = requests.get(
        url,
        headers=headers,
        data=request_body,
    )

print(r)