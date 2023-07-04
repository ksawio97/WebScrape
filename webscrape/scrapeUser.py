from .data.info import Info
from . import scrape

import json

#TO DO delete this functions and create one that will get data from db and then look for accounts
def instagramInfo(name: str) -> Info:
    url = f"https://www.instagram.com/{name}" 
    soup = scrape.getSoupPageContent(url)
    if soup == None: return None
    
    result = scrape.scrape(soup, "script", {"type": "application/ld+json"})
    if result == None:
        return None
    jsonResult = json.loads(result.string)

    return Info(name=jsonResult["author"]["name"], description=jsonResult["description"], image=jsonResult["author"]["image"], url=url)

def githubInfo(name: str) -> Info:
    url = f"https://github.com/{name}" 
    soup = scrape.getSoupPageContent(url)
    if soup == None: return None

    return Info(
        name = name,
        description = scrape.scrape(soup, "meta", {"name": "description"}, "")["content"],
        image = scrape.scrape(soup, "meta", {"name": "twitter:image:src"})["content"],
        url = url)

def twitchInfo(name: str) -> Info:
    url = f"https://www.twitch.tv/{name}" 
    soup = scrape.getSoupPageContent(url)
    if soup == None: return None

    desciptionResult = scrape.scrape(soup, "meta", {"name": "twitter:description"})
    imageResult = scrape.scrape(soup, "meta", {"name": "twitter:description"})

    if desciptionResult is None or  imageResult is None: return None
    return Info(
        name = name,
        description = desciptionResult["content"],
        image = imageResult["content"],
        url = url
    )

def steamInfo(name: str) -> Info:
    url = f"https://steamcommunity.com/id/{name}"
    soup = scrape.getSoupPageContent(url)
    if soup == None: return None

    nameResult = scrape.scrape(soup, "meta", {"property": "twitter:title"})
    desciptionResult = scrape.scrape(soup, "meta", {"property": "twitter:description"})
    imageResult = scrape.scrape(soup, "meta", {"name": "twitter:image"})

    if nameResult is None or  imageResult is None: return None
    return Info(
        name = nameResult["content"] if nameResult is not None else "",
        description = desciptionResult["content"] if desciptionResult is not None else "",
        image = imageResult["content"] if imageResult is not None else "",
        url = url
    )