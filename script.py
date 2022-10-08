import requests
from dotenv import load_dotenv
import os

load_dotenv()

bbbUSERNAME = os.environ["bbbUSERNAME"]
bbbPASSWORD = os.environ["bbbPASSWORD"]

url = 'https://api.bbb.org/token'
headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
    }
r = requests.post(
        url,
        headers=headers
    )