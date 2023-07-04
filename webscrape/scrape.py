import bs4
import requests

def scrape(soup: bs4.BeautifulSoup, tag: str, args: dict, emergencyReturnValue=None):
    result = soup.find(tag, attrs=args) 
    return result if result else emergencyReturnValue

def getSoupPageContent(url):
    response = requests.get(url)
    return bs4.BeautifulSoup(response.content, "html.parser")