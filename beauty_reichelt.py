#!/usr/bin/python3

from bs4 import BeautifulSoup
import requests

query = input("Look for any article: ").replace(" ", "+")


base_url = "https://reichelt.de"

# Search "string".
url = "https://reichelt.de/de/de/index.html?ACTION=446&LA=2&nbc=1&q="

# List 100 articles, with price low-to-high.
parameter = "&SID=96640de05955b2454a545a04b307331c3ff873043bd18d20ae0b1"


mix = url + query + parameter

print(mix)


# Will not work without these headers.
headers = {
	#"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    #"Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "de-DE,en-US;q=0.7,en;q=0.3",
    "Connection": "keep-alive",
    "DNT": "1",
    "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:86.0) Gecko/20100101 Firefox/86.0",

	
}


artlinks = []
info = []
prices = []
versand = []

r = requests.get(mix, headers = headers)

if r.status_code == 200:
	print("\033[33m\nFetching results...")
	
else:
	print("Connection with Reichelt.de not established. \n")
	print(r.status_code)

html = r

soup = BeautifulSoup(html.content, "html.parser")


# Inspect element on Firefox.
art_link = soup.find_all(class_="al_artinfo_link")

preis = soup.find_all(class_="itemprop")

versand_infos = soup.find_all( class_="status_1")

description = soup.find_all(class_="al_artinfo_headline")




for art in art_link:
	#print(art["href"])
	artlinks.append(art["href"])

for e in preis:
	#print(e.string)
	prices.append(e.string)


for vers in versand_infos:
	#print(vers.text)
	versand.append(vers.text)
	
	
for desc in description:
	#print(desc.text)
	info.append(desc.text)




for i, ii, iii, iv in zip(info, versand, prices, artlinks):
	print("{0} Versand: {1} \n Price: {2} \n {3}".format(i, ii, iii, iv))
