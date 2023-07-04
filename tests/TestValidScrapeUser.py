from context import scrapeUser
import unittest

#!!! results depend on accounts existing (they should exist)
class TestValidScrapeUser(unittest.TestCase):
    def test_instagramInfo(self):
        info = scrapeUser.instagramInfo("instagram")
        self.infoIsNotNone(info)
    
    def test_githubInfo(self):
        info = scrapeUser.githubInfo("github")
        self.infoIsNotNone(info)
    
    def test_twitchInfo(self):
        info = scrapeUser.twitchInfo("twitch")
        self.infoIsNotNone(info)

    def infoIsNotNone(self, info):
        self.assertIsNotNone(info)
        self.assertIsNotNone(info.name)
        self.assertIsNotNone(info.image)
        self.assertIsNotNone(info.description)
        self.assertIsNotNone(info.url)

if __name__ == '__main__':
    unittest.main()