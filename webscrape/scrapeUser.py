from .data.info import Info
from . import scrape

import re

def readInfo(username: str, websiteInfo: dict) -> Info:
    url = websiteInfo["url"].replace("{}", username)
    soup = scrape.getSoupPageContent(url)
    if soup == None: return None

    info = Info(name=websiteInfo["name"], url=url, username=None, description=None)
    if "scrape" not in websiteInfo.keys(): return info

    for _, (key, scrapeInfo) in enumerate(websiteInfo["scrape"].items()):
        result = scrape.scrape(soup, scrapeInfo["tag"], {scrapeInfo["findId"]: scrapeInfo["findValue"]})
        keys = scrapeInfo.keys()
        #sometimes errorValue is not finding result
        if result is None:
            if "errorValue" in keys and scrapeInfo["errorValue"] == str(None):
                return None
            continue
        
        #user not found! (bsc of special error)
        if "errorValue" in keys and scrapeInfo["errorValue"] == result["content"]: 
            return None

        if "regex" in keys:
            content = re.match(scrapeInfo["regex"], result['content'])
        else:
            content = result['content']
        
        exec(f"info.{key} = '{content}'")

    if info.username is None:
        info.username = username

    return info