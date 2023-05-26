import requests
from bs4 import BeautifulSoup
import pandas as pd


urls = ["http://books.toscrape.com/catalogue/page-{}.html".format(i) for i in range(1,51)]

def clean_scrape(book):
    info= {}
        
    info['image_url'] = book.find('img')['src']
    info['book_title'] = book.find('h3').find('a')['title']
    info['product_price'] = book.find('p',{'class': 'price_color'}).text
        
    return info
def get_books(url):
	r = requests.get(url)
	htmlContent = r.content
	soup = BeautifulSoup(htmlContent, 'html.parser')
	page = soup.find_all('li', {'class': "col-xs-6 col-sm-4 col-md-3 col-lg-3"})
	to_dicts = [clean_scrape(book) for book in page]
    
	return to_dicts

all_dicts = []

for url in urls:
    all_dicts.extend(get_books(url))

df = pd.DataFrame(all_dicts)
df.to_csv('Challenge - Scrape a Book Store!.csv')
