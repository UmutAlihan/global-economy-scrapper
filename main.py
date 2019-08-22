from html5print import HTMLBeautifier as htmlb
import re
import csv
import urllib.request
import requests
import pandas as pd
from bs4 import BeautifulSoup
import os, ssl
if (not os.environ.get('PYTHONHTTPSVERIFY', '') and
    getattr(ssl, '_create_unverified_context', None)): 
    ssl._create_default_https_context = ssl._create_unverified_context

	

#Country - All Years - All Indicators
url = "http://wits.worldbank.org/data/public/cp/en_USA_allyears_wits_trade_summary.csv"
response = requests.get(url, verify=False)

alihan = requests.get(url, verify=False)
with open("C:\Users\umdikel\Desktop\local\Alihan\global-economy-scrapper\test.csv", "wb") as f:
	f.write(alihan.content)
	


	

#TR : 2016	
#https://wits.worldbank.org/CountryProfile/en/Country/TUR/Year/2016/Summary	


"""def download_file(url, filename):
	''' Downloads file from the url and save it as filename '''
	# check if file already exists
	if not os.path.isfile(filename):
		print('Downloading File')
		response = requests.get(url,verify=False)
		# Check if the response is ok (200)
		if response.status_code == 200:
			# Open file and write the content
			with open(filename, 'wb') as file:
			# A chunk of 128 bytes
				for chunk in response:
					file.write(chunk)
		else:
			print('File exists')""""	