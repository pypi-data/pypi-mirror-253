from bs4 import BeautifulSoup
import requests

def getCompanyInfo(ttName):
    """Returns company info of the ttName"""
    res = requests.get("https://www.tickertape.in/stocks/{}".format(ttName))
    soup = BeautifulSoup(res.content, "html.parser")
    ticker = soup.find("span", {"class":"ticker"}).text
    name = soup.find("h1", {"class":"security-name"}).text
    price = soup.find("span", {"class":"current-price"}).text
    return {
        "ttName": ttName,
        "name": name,
        "ticker": ticker,
        "price": price
    }

def getTopCompanies():
    """Returns the list of ttName of top companies"""
    res = requests.get("https://www.tickertape.in/stocks?filter=top")
    soup = BeautifulSoup(res.content, "html.parser")
    
    pageDiv = soup.find("div", {"class":"page"})
    lis = pageDiv.find_all("li")
    
    topCompanies = []
    for li in lis:
        ttName = li.find("a").get("href").split("/stocks/")[-1]
        topCompanies.append(ttName)
    return topCompanies

def getAllCompanies():
    """Returns the list of ttName of all companies"""
    res = requests.get("https://www.tickertape.in/stocks")
    soup = BeautifulSoup(res.content, "html.parser")
    links_div = soup.find("div", {"class":"link-list"})
    alinks = links_div.find_all("a")
    
    allCompanies = set()
    for alink in alinks:
        ares = requests.get("https://www.tickertape.in/stocks?filter={}".format(alink.text))
        asoup = BeautifulSoup(ares.content, "html.parser")
        
        pageDiv = asoup.find("div", {"class":"page"})
        if not pageDiv: continue
        lis = pageDiv.find_all("li")
    
        for li in lis:
            ttName = li.find("a").get("href").split("/stocks/")[-1]
            if len(ttName.split("/etfs/")) > 1: continue
            allCompanies.add(ttName)
    return list(allCompanies)