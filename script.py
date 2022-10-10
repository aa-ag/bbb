from dotenv import load_dotenv
import requests
import os
import json
import datetime

load_dotenv()

bbbUSERNAME = os.environ["bbbUSERNAME"]
bbbPASSWORD = os.environ["bbbPASSWORD"]


def authenticate():
    '''
     in compliance with the documentation, 
     before making any calls to the api,
     using a pre-registered username & password, 
     a token is generated.

     response = {
        "access_token": x,
        "token_type": y,
        "expires_in": z,
        "userName": a,
        "authGuid": b,
        "maxRequestsForMonthPeriod": c,
        "maxRequestsForDayPeriod": d,
        "maxRequestsForHourPeriod": e,
        "maxRequestsForMinutePeriod": f,
        "maxRecordsForMonthPeriod": g,
        ".issued": h,
        ".expires": j,
    }
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
        authentication_data = json.loads(r.content)
        return authentication_data
    else:
        print(r.status_code, r.headers, r.content)
        return


def search_org(bbb_token=None):
    '''
     generate authentication token,
     and search for an org by paramenter `businessUrl`
    '''
    
    url = "https://api.bbb.org/api/orgs/search?businessUrl=https://www.zendesk.com/"
    
    headers = {
            'Authorization': f'Bearer {bbb_token}',
            'content-Type': 'application/x-www-form-urlencoded'
        }

    r = requests.get(url,headers=headers)

    print(r.headers)
    print(r.content)


if __name__ == "__main__":
    authentication_data = authenticate()
    search_org(authentication_data["access_token"])