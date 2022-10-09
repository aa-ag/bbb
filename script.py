import requests
from dotenv import load_dotenv
import os
import json

load_dotenv()

bbbUSERNAME = os.environ["bbbUSERNAME"]
bbbPASSWORD = os.environ["bbbPASSWORD"]
bbbTOKEN = os.environ["bbbTOKEN"]


def authenticate():
    url = 'https://api.bbb.org/token'

    headers = {
            'Authorization': f'Bearer {bbbTOKEN}',
            'content-Type': 'application/x-www-form-urlencoded'
        }

    request_body = "grant_type=password&username={0}&password={1}".format(
        bbbUSERNAME, bbbPASSWORD
    )

    r = requests.get(
            url,
            headers=headers,
            data=request_body,
        )

    print(r)


if __name__ == "__main__":
    authenticate()