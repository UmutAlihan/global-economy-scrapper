import csv
import urllib.request
import requests
import pandas as pd
from bs4 import BeautifulSoup
import os, ssl
import xlwings as xw
import time
if (not os.environ.get('PYTHONHTTPSVERIFY', '') and
    getattr(ssl, '_create_unverified_context', None)): 
    ssl._create_default_https_context = ssl._create_unverified_context


	

#Country - All Years - All Indicators
wb = xw.Book("C:\\Users\\umdikel\\Desktop\\local\\Alihan\\global-economy-scrapper\\ulke-kisaltma.xlsx")
ws = wb.sheets[0]
abr_list = ws.range('A2:A198').value

for country in abr_list:
  time.sleep(1)
  country = country.strip()
  print(country)
  url = "http://wits.worldbank.org/data/public/country_profile_at_a_glance/en_" + country + "_at-a-glance.CSV"
  response = requests.get(url, verify=False)
  csv_file = "C:\\Users\\umdikel\\Desktop\\local\\Alihan\\global-economy-scrapper\\Data\\Summary-" + country+ ".csv"
  with open(csv_file, "wb") as f:
    f.write(response.content)
