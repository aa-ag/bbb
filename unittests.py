import unittest
from dotenv import load_dotenv
import os

load_dotenv()

class TestScript(unittest.TestCase):
    def test_username_exists(self):
        bbbUSERNAME = os.environ["bbbUSERNAME"]

        self.assertIsNotNone(bbbUSERNAME)
    
    def test_password_exists(self):
        bbbPASSWORD = os.environ["bbbPASSWORD"]

        self.assertIsNotNone(bbbPASSWORD)



if __name__ == "__main__":
    unittest.main()