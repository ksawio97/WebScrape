from context import scrapeUser
import unittest

#!!! results depend on accounts existing (they shouldn't exist)
probablyInValidAccount = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
class TestInValidScrapeUser(unittest.TestCase):
    def test_instagramInfo(self):
        info = scrapeUser.instagramInfo(probablyInValidAccount)
        self.assertIsNone(info)
    
    def test_githubInfo(self):
        info = scrapeUser.githubInfo(probablyInValidAccount)
        self.assertIsNone(info)
    
    def test_twitchInfo(self):
        info = scrapeUser.twitchInfo(probablyInValidAccount)
        self.assertIsNone(info)

    def test_steamInfo(self):
        info = scrapeUser.steamInfo(probablyInValidAccount)
        self.assertIsNone(info)

if __name__ == '__main__':
    unittest.main()