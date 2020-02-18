import requests
from bs4 import BeautifulSoup
import urllib.request
import mysql.connector
from sys import argv

cihazexport = open("butuncihazlar.txt", "wb")
url = "https://www.kimovil.com/sitemaps/sitemap.en.xml"
headers = {'User-Agent': 'Mozilla/5.0'}
url_oku = requests.get(url, headers=headers)
html_content = url_oku.text
soup = BeautifulSoup(html_content,'lxml')
print("Bütün cihazların listesi güncelleniyor...")

for cihazyazilacak in soup.find_all('loc'):    
  cihazexport = open("butuncihazlar.txt", "ab")
  if ("where-to-buy" in str(cihazyazilacak.text.strip())):
    cihazexport.write(str(cihazyazilacak.text.strip()).encode('utf-8'))
    cihazexport.write(str("\n").encode('utf-8'))
 
print("Cihazların listesi güncellendi.")