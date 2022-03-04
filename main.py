
#import quiz
#quiz.quiz()

from web_scrape import scraping_mossblanc_lists
from web_scrape import scraping_mossblanc_list_one_by_one_save_csv
mainUrl = 'https://smartstore.naver.com/mossblanc/'
index_list = scraping_mossblanc_lists(mainUrl)
scraping_mossblanc_list_one_by_one_save_csv(index_list)