### libraries
import unittest
from dotenv import load_dotenv
import os
import requests
from bs4 import BeautifulSoup
### relative imports
from script import search_org, scrape_bbb_profile, authenticate
from db import connect_to_db

### global
load_dotenv()

bbbUSERNAME = os.environ["bbbUSERNAME"]
bbbPASSWORD = os.environ["bbbPASSWORD"]
bbb_token = os.environ["bbb_token"]

### Tests
class TestScript(unittest.TestCase):
    ### .env / global/env variables required
    def test_username_exists(self):
        self.assertIsNotNone(bbbUSERNAME)
    
    def test_password_exists(self):
        self.assertIsNotNone(bbbPASSWORD)

    def test_token_exists(self):
        self.assertIsNotNone(bbb_token)

    ### db
    def test_db_connection(self):
        connection = connect_to_db()
        cursor = connection.cursor()
        cursor.execute("SELECT version();")
        db_version = cursor.fetchone()
        expected_db_version='PostgreSQL 13.6 (Ubuntu 13.6-1.pgdg20.04+1) on x86_64-pc-linux-gnu, compiled by gcc (Ubuntu 9.3.0-17ubuntu1~20.04) 9.3.0, 64-bit'
        self.assertEqual(db_version[0],expected_db_version)

    ### functions
    # def test_authenticate(self):
    #     a = authenticate()
    #     self.assertEqual(a, 200)

    # def test_search_org(self):
    #     chosen_parameter = "businessUrl"
    #     parameter_input = "https://zendesk.com/"
    #     expected_bbb_url = "https://www.bbb.org/us/ca/san-francisco/profile/computer-software-developers/zendesk-1116-377060"
    #     found_bbb_url = search_org(bbb_token,chosen_parameter,parameter_input)
    #     self.assertEqual(expected_bbb_url, found_bbb_url)

    # def test_scrape_bbb_profile(self):
    #     test_bbb_url = "https://www.bbb.org/us/ca/san-francisco/profile/computer-software-developers/zendesk-1116-377060"
    #     rating = scrape_bbb_profile(test_bbb_url)
    #     self.assertEqual(rating, "D-")

### Driver
if __name__ == "__main__":
    unittest.main()