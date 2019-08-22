import csv
import urllib.request
#import ssl
#ssl._create_default_https_context = ssl._create_unverified_context
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
