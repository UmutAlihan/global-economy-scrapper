from html5print import HTMLBeautifier as htmlb
import re
import csv
import urllib.request
from bs4 import BeautifulSoup
import os, ssl
if (not os.environ.get('PYTHONHTTPSVERIFY', '') and
    getattr(ssl, '_create_unverified_context', None)): 
    ssl._create_default_https_context = ssl._create_unverified_context
atra = open('trial.csv', 'w', newline = '')
writer = csv.writer(atra)
soup = BeautifulSoup(urllib.request.urlopen("https://wits.worldbank.org/countrysnapshot/en/TUR").read(), 'lxml')

tbody = soup('table', {"class":"alignRight data"})[0].find_all('tr')
for row in tbody:
    cols = row.findChildren(recursive=False)
    cols = [ele.text.strip() for ele in cols]
    writer.writerow(cols)
    print(cols)

	
#TR : 2016	
#https://wits.worldbank.org/CountryProfile/en/Country/TUR/Year/2016/Summary	
	
	

"""def compare(row):
	left = soup('td', {"class":"alignLeft data"})[row]
	right = soup('td', {"class":"alignRight data"})[row]
	return(left,right)"""
	

"""left = soup('td', {"class":"alignLeft data"})
right = soup('td', {"class":"alignRight data"})"""
	
	
"""table_striped = soup('table', {"class":"table table-striped"})

gdp = re.compile("GDP")

for item in table_striped:
	item.find_all("GDP")"""

