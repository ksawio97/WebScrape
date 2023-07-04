import unittest

import TestInValidScrapeUser
import TestValidScrapeUser

if __name__ == "__main__":
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()

    suite.addTests(loader.loadTestsFromModule(TestInValidScrapeUser))
    suite.addTests(loader.loadTestsFromModule(TestValidScrapeUser))

    result = unittest.TextTestRunner().run(suite)