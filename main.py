from webscrape import scrapeUser
from webscrape import target

import threading
import json

def FindUser(searchTarget: str, websiteInfo: dict):
    result = scrapeUser.readInfo(searchTarget, websiteInfo)
    if result is not None:
        print(result)

if __name__ == "__main__":
    searchTarget = target.getTarget()
    #read websites
    websites = None
    with open(".db/websites.json", "r") as fh:
        websites = json.load(fh)

    threads = []
    for _, (_, v) in enumerate(websites.items()):
        threads.append(threading.Thread(target=FindUser, args=(searchTarget, v)))
        threads[-1].start()

    #wait for threads
    for thread in threads:
        thread.join()