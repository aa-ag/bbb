import requests
from dotenv import load_dotenv
import os
import json

load_dotenv()

bbbUSERNAME = os.environ["bbbUSERNAME"]
bbbPASSWORD = os.environ["bbbPASSWORD"]


def authenticate():
    '''
     in compliance with the documentation, 
     before making any calls to the api,
     using a pre-registered username & password, 
     a token is generated.
    '''
    url = 'https://api.bbb.org/token'

    header = {
            'content-type': 'application/x-www-form-url-encoded'
        }

    request_body = "grant_type=password&username={0}&password={1}".format(
        bbbUSERNAME, bbbPASSWORD
    )

    r = requests.post(
            url,
            headers=header,
            data=request_body,
        )

    if r.status_code == 200:
        contents = json.loads(r.content)
        authentication_token = contents["access_token"]
        return authentication_token
    else:
        print(r.status_code, r.headers, r.content)
        return


def search_org():
    url = "https://api.bbb.org/api/orgs/search"
    headers = {
            'Authorization': f'Bearer {bbbTOKEN}',
            'content-Type': 'application/x-www-form-urlencoded'
        }

    request_body = "grant_type=password&username={0}&password={1}".format(
        bbbUSERNAME, bbbPASSWORD
    )

    r = requests.get(url,headers=headers,data=request_body)

    print(r.headers)
    print(r.content)


if __name__ == "__main__":
    search_org()