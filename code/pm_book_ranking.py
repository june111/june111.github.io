import requests
from bs4 import BeautifulSoup

import csv

# get book list from csv
book_list = []
with open('index.csv', newline='') as csv_file:
	spamreader = csv.reader(csv_file)
	for row in spamreader:
 		book_list.append(row)

book_list_len = len(book_list)
print(book_list_len)

i=0
while i < book_list_len:
  print(i)
  target_book = " ".join(book_list[i])
  print(target_book)
  URL = 'https://www.goodreads.com/search?q='+target_book+'&search_type=books'

  # use your usable proxies here
  # replace host with you proxy IP and port with port number
  proxy_IP='http://169.57.1.84:25'
  proxies = { 'http': proxy_IP, 
              'https': proxy_IP} 

  page = requests.get(URL, proxies=proxies, verify=False)
  
  print('Response:', page)

  soup = BeautifulSoup(page.content, 'html.parser')


  book_title_tap = soup.find("a", class_="bookTitle")
  author_name_tap = soup.find("a", class_="authorName")
  info_tap = soup.find("span", class_="greyText smallText uitext")

  # 文本处理
  book_title = book_title_tap.text.strip()
  author_name = author_name_tap.text.strip()
  info_block = info_tap.text.strip()
  info = info_block.splitlines()
  rating = info[0][:4]
  people = info[0][18:].replace('ratings','').strip()
  if len(info)>3:
    published = info[3].strip()
  else:
    published = ''

  # print(book_title)

  # export

  # open a csv file with append, so old data will not be erased
  with open('pm_book.csv', 'a', newline='') as csv_file:
   writer = csv.writer(csv_file)
   writer.writerow([book_title, author_name, rating, people, published])
  i += 1

print('CSV already done in the same file with the code')


