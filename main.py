from webscrape import scrapeUser
from webscrape import target

searchTarget = target.getTarget()
if __name__ == "__main__":
    info = scrapeUser.instagramInfo(searchTarget)
    print(info)

    info = scrapeUser.githubInfo(searchTarget)
    print(info)

    info = scrapeUser.twitchInfo(searchTarget)
    print(info)