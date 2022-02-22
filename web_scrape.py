from bs4 import BeautifulSoup
import requests
def scrape_func():
  default_url = 'https://smartstore.naver.com'
  url = 'https://smartstore.naver.com/mossblanc/'
  req = requests.get(url)
  soup = BeautifulSoup(req.content,'html.parser')
  print(soup.title)
  lists = soup.find_all('a')
  pages = []
  for ix in range(0, len(lists)):
    list = lists[ix].get('href')
    pages.append(list)
    print(f"list {ix} :{list}")
  subpage = []
  for p in range(0,len(pages)):
    if "mossblanc/products" in pages[p]:
        pullurl = default_url + pages[p]
        print(f"subpage {p}: {pullurl}")    
        subpage.append(pullurl)
      