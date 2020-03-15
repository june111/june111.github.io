import requests
from bs4 import BeautifulSoup

target_book = 'management'
URL = 'https://www.goodreads.com/search?q='+target_book+'&search_type=books'

# use your usable proxies here
# replace host with you proxy IP and port with port number
proxy_IP='http://169.57.1.84:25'
proxies = { 'http': proxy_IP, 
            'https': proxy_IP} 

page = requests.get(URL, proxies=proxies)
print('Response:', page)

soup = BeautifulSoup(page.content, 'html.parser')

book_title_tap = soup.find("a", class_="bookTitle")

# 文本处理
book_title = book_title_tap.text.strip()

print(book_title)

import csv

# open a csv file with append, so old data will not be erased
with open('index.csv', 'a', newline='') as csv_file:
 writer = csv.writer(csv_file)
 writer.writerow([book_title])

print('CSV already done in the same file with the code')


