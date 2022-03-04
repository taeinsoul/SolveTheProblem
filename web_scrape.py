from bs4 import BeautifulSoup
import requests
import csv

default_url = 'https://smartstore.naver.com'

def scrape_func(url):
  req = requests.get(url)
  soup = BeautifulSoup(req.content,'html.parser')
  lists = soup.find_all('a')
  pages = []
  for ix in range(0, len(lists)):
    list = lists[ix].get('href')
    if list.find("products") != -1:
      pages.append(list)
      
  subpage = []
  for p in range(0,len(pages)):
    if "mossblanc/products" in pages[p]:
        pullurl = default_url + pages[p]
        #print(f"list {p}: {pullurl}")    
        subpage.append(pullurl)
  return subpage

def scraping_mossblanc_lists(WebUrl):
  request = requests.get(WebUrl)
  soupListData = BeautifulSoup(request.content,'html.parser')
  contentsList = soupListData.find_all('a','_3HQCww4jR6')
  index_lists = []
  for list in contentsList:
    print(list.get_text())
    FullUrl = default_url+list.get('href')
    index_lists.append([list.get_text(), FullUrl])
  return index_lists

def scraping_mossblanc_list_one_by_one_save_csv(lists):
  f = open('output.csv', 'w', encoding='utf-8', newline='')
  wr = csv.writer(f)
  
  for item in lists:
    wr.writerow([item[0]])
    for url in scrape_func(item[1]):
      wr.writerow([url])
    