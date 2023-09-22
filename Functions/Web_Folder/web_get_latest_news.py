import requests
from bs4 import BeautifulSoup
import gzip
import urllib

# Dated 20 Feb 2023 #

# Main function is get_latest_news_sg(). Takes news headlines from local news websites and returns a list of news headlines.
# Returns a list of 2 by 1. [Headline string, link]

def get_latest_news_sg():

    # CNA HEADLINES #

    url = "https://www.channelnewsasia.com/"
    r = requests.get(url)
    soup = BeautifulSoup(r.content, "html.parser")

    CNA_headlines = []
    for h in soup.find_all("a", {"class": "h6__link list-object__heading-link"}):
        headline = h.text.strip()
        link = h.get('href')
        source = "CNA"
        CNA_headlines.append((f"{headline} - {source}", url + link))

    # TODAY HEADLINES #

    url = "https://www.todayonline.com/"
    r = requests.get(url)
    soup = BeautifulSoup(r.content, "html.parser")

    TODAY_headlines = []
    for h in soup.find_all("a", {"class": "h4__link list-object__heading-link"}):
        headline = h.text.strip()
        link = h.get('href')
        source = "TODAY"
        TODAY_headlines.append((f"{headline} - {source}", url + link))

    # Strait Times Headlines #

    url = "https://www.straitstimes.com/"
    headers = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'en-US,en;q=0.5',
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:38.0) Gecko/20100101 Firefox/38.0'}
    req = urllib.request.Request(url, headers=headers)
    response = urllib.request.urlopen(req)
    pagedata = gzip.decompress(response.read())
    souped = BeautifulSoup(pagedata, "html.parser")

    STRAITS_headlines = []
    for h in souped.find_all("a", {"class": "stretched-link"}):
        headline = h.text.strip()
        if headline == "":
            headline = "Interactive Link"
        link = h.get('href')
        source = "Strait Times"
        STRAITS_headlines.append((f"{headline} - {source}", url + link))

    # YAHOO NEWS HEADLINES #

    url = "https://sg.news.yahoo.com/"
    r = requests.get(url)
    soup = BeautifulSoup(r.content, "html.parser")
    YAHOO_headlines = []
    for h in soup.find_all("u", {"class": "StretchedBox"}):
        headline = h.parent.text.strip()
        link = h.parent.get('href')
        source = "YAHOO NEWS"
        YAHOO_headlines.append((f"{headline} - {source}", url + link))

    COMBINED_HEADLINES = []
    COMBINED_HEADLINES.extend(CNA_headlines)
    COMBINED_HEADLINES.extend(TODAY_headlines)
    COMBINED_HEADLINES.extend(STRAITS_headlines)
    COMBINED_HEADLINES.extend(YAHOO_headlines)
    COMBINED_HEADLINES.sort(key=lambda x: x[0])

    return COMBINED_HEADLINES
