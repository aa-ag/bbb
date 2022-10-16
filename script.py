### TODO: 
    ### - try except instead of making requests that may fail
    ### - translate into javascript to create chrome extension


############------------ IMPORTS ------------##################################
from dotenv import load_dotenv
import requests
import os
import json
from bs4 import BeautifulSoup
from pprint import pprint
import re

############------------ GLOBAL VARIABLE(S) ------------#######################
load_dotenv()

bbbUSERNAME = os.environ["bbbUSERNAME"]
bbbPASSWORD = os.environ["bbbPASSWORD"]

bbb_token = os.environ["bbb_token"]

############------------ FUNCTION(S) ------------##############################
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
        authentication_data = r.json()
        with open(".env", "w") as f:
            f.write(
                f"bbbUSERNAME=\'{bbbUSERNAME}\'\nbbbPASSWORD=\'{bbbPASSWORD}\'\nbbb_token=\'{authentication_data['access_token']}\'"
            )
    else:
        print(r.status_code, r.headers, r.content)
        return


def search_org(bbb_token,chosen_parameter,parameter_input):
    '''
     generate authentication token,
     and search for an org by parameter `businessUrl`

     response object has 3 properties:
        - TotalResults
        - PageNumber
        - SearchResults

        and each object within the list of results contains:
        'BusinessId', 'BureauCode', 'OrganizationName', 
        'PrimaryCategory', 'ReportURL', 'City', 'StateProvince', 
        'Phones', 'BusinessURLs', 'Address', 'AltOrganizationNames', 
        'OrganizationType', 'OrgId', 'OrganizationLastChanged', 
        'RatingLastChanged', 'AccreditationStatusLastChanged', 
        'IsICEParticipant', 'ExcludeFromFindALocation', 
        'ComplaintCloseTypeCount', 'ComplaintType', 'LicenseDetails', 
        'RatingIcons', 'ProfileUrl', 'BbbFileOpenDate', 'TypeOfEntity', 
        'IncorpStateCode', 'IncorpCountryCode', 'IncorporationDate', 
        'CustomerContacts', 'Statistics', 'Alerts', 'CustomTexts', 
        'IncorporatedState', 'IncorporatedYear', 'LatLng'
    '''
    
    url = "https://api.bbb.org/api/orgs/search?{0}={1}".format(
        chosen_parameter,
        parameter_input
    )
    print(url)
    headers = {
            'Authorization': f'Bearer {bbb_token}',
            'content-Type': 'application/x-www-form-urlencoded'
        }

    r = requests.get(url,headers=headers).json()

    if r["TotalResults"] < 1:
        return "No results"
    
    search_results = r["SearchResults"]
    # pprint(search_results)
    for result in search_results:
        return result["ProfileUrl"]


def scrape_bbb_profile(bbb_url):
    '''
     scrape the main/official BBB profile 
     of a business found by ProfileUrl, and
     create a soup with the HTML of the page, 
     and find the rating for that business
    '''
    headers = {
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246"
    }
    page = requests.get(
        bbb_url,
        headers=headers
    )

    soup = BeautifulSoup(page.content, 'html.parser')
    rating_spam = soup.find_all(
        "span", 
        {"class": "dtm-rating bg-gray-40 leading-1 text-blue-brand css-o3tnwk ez39sfa0"})
    rating_tag = str(rating_spam[0].next)
    rating = re.sub(r'<.*?>', '', rating_tag)
    print(rating)
    return rating


############------------ DRIVER CODE ------------##############################
if __name__ == "__main__":
    chosen_parameter = "businessUrl"
    parameter_input = "https://www.google.com"
    # bbb_token = authenticate()
    bbb_url = search_org(bbb_token,chosen_parameter,parameter_input)
    print(bbb_url)
    scrape_bbb_profile(bbb_url)

