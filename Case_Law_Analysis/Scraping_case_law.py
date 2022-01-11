from bs4 import BeautifulSoup
import requests

URL = 'https://www.epant.gr/apofaseis-gnomodotiseis/itemlist/category/78-2021.html'
proxy = 'http://78.130.136.2:8080'

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36", 
    "X-Amzn-Trace-Id": "Root=1-61acac03-6279b8a6274777eb44d81aae", 
    "X-Client-Data": "CJW2yQEIpLbJAQjEtskBCKmdygEIuevKAQjr8ssBCOaEzAEItoXMAQjLicwBCKyOzAEI3I7MARiOnssB" }
page = requests.get(URL, headers = headers)
soup = BeautifulSoup(page.content,'html.parser')

baseUrl = 'https://www.epant.gr'

for href in [x['href'] for x in soup.select('a[href*=category]:has(span)')]:
    page = requests.get(f'{baseUrl}{href}', headers = headers)
    soup = BeautifulSoup(page.content,'html.parser')

    urls = [f'{baseUrl}{x["href"]}' for x in soup.select('h3 a')]

    for url in urls :
        page = requests.get(url, headers = headers)
        soup = BeautifulSoup(page.content,'html.parser')
        row = soup.find('td', text = "Ένδικα Μέσα").parent.get_text(strip=True) if soup.find('td', text = "Ένδικα Μέσα") else None
        case = soup.find('h2').text.strip()
        year = case.split('/')[-1]
        print(f'{year},{case},{row},{url}')
