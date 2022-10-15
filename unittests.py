import unittest

class TestScript(unittest.TestCase):
    def is_there_a_token(self):
        from dotenv import load_dotenv
        import os
        
        load_dotenv()

        bbbUSERNAME = os.environ["bbbUSERNAME"]

        self.assertIsNotNone(bbbUSERNAME)


if __name__ == "__main__":
    unittest.main()