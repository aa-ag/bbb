import unittest
from dotenv import load_dotenv
import os
from script import search_org

load_dotenv()

bbbUSERNAME = os.environ["bbbUSERNAME"]
bbbPASSWORD = os.environ["bbbPASSWORD"]
bbb_token = os.environ["bbb_token"]

class TestScript(unittest.TestCase):
    ### .env / global/env variables required
    def test_username_exists(self):
        self.assertIsNotNone(bbbUSERNAME)
    
    def test_password_exists(self):
        self.assertIsNotNone(bbbPASSWORD)

    def test_token_exists(self):
        self.assertIsNotNone(bbb_token)

    ### functions
    def test_search_org(self):
        chosen_paramenter = "businessUrl"
        paramenter_input = "https://zendesk.com/"
        expected_bbb_url = "https://www.bbb.org/us/ca/san-francisco/profile/computer-software-developers/zendesk-1116-377060"
        found_bbb_url = search_org(bbb_token,chosen_paramenter,paramenter_input)
        self.assertEqual(expected_bbb_url, found_bbb_url)

if __name__ == "__main__":
    unittest.main()