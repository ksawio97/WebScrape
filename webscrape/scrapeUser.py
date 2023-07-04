from .data.info import Info
from . import scrape

import json

def instagramInfo(name: str) -> Info:
    url = f"https://www.instagram.com/{name}" 
    soup = scrape.getSoupPageContent(url)

    result = scrape.scrape(soup, "script", {"type": "application/ld+json"})
    if result == None:
        return None
    jsonResult = json.loads(result.string)

    return Info(name=jsonResult["author"]["name"], description=jsonResult["description"], image=jsonResult["author"]["image"], url=url)

def githubInfo(name: str) -> Info:
    url = f"https://github.com/{name}" 
    soup = scrape.getSoupPageContent(url)

    if soup.contents[0] == "Not Found": return None

    return Info(
        name = name,
        description = scrape.scrape(soup, "meta", {"name": "description"}, "")["content"],
        image = scrape.scrape(soup, "meta", {"name": "twitter:image:src"})["content"],
        url = url)

def twitchInfo(name: str) -> Info:
    url = f"https://www.twitch.tv/{name}" 
    soup = scrape.getSoupPageContent(url)

    desciptionResult = scrape.scrape(soup, "meta", {"name": "twitter:description"})
    imageResult = scrape.scrape(soup, "meta", {"name": "twitter:description"})

    if desciptionResult is None or  imageResult is None: return None
    return Info(
        name = name,
        description = scrape.scrape(soup, "meta", {"name": "twitter:description"})["content"],
        image = scrape.scrape(soup, "meta", {"name": "twitter:image"})["content"],
        url = url
    )