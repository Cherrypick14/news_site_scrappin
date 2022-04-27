import unittest
from main import uri_validator


class TesTNewsScrapText(unittest.TestCase):
    def test_uri_validator(self):
        self.assertTrue(uri_validator("https://www.bbc.com/news"))
        self.assertFalse(uri_validator(""))
        self.assertFalse(uri_validator("ds"))
        self.assertFalse(uri_validator(0))
        self.assertFalse(uri_validator("/data/Python.html"))

if __name__== "__main__":
    unittest.main()