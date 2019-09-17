#Nice Modules
		#General List
		#https://mode.com/blog/python-data-visualization-libraries
		#Geoplotlib
		#https://github.com/andrea-cuttone/geoplotlib

#Following this intro tutorial https://towardsdatascience.com/visualising-economic-data-using-plotly-a07f96f58160

import pandas as pd
import os
import matplotlib.pyplot as plt
import seaborn as sns
#%matplotlib inline
from bubbly.bubbly import bubbleplot
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
import plotly as pyimport plotly.graph_objs as go
init_notebook_mode(connected=True) #do not miss this linefrom plotly import tools


data = pd.read_csv("C:\\Users\\umdikel\\Desktop\\local\\Alihan\\global-economy-scrapper\\Data\\Summary-TUR.csv")

data_dir = "C:\\Users\\umdikel\\Desktop\\local\\Alihan\\global-economy-scrapper\\Data\\"
for file in os.listdir(data_dir):
	print(file)
	try:
		data = pd.read_csv(data_dir + file)
		indic_data = data.loc[data["Indicator"].isin(["GDP (current US$ Mil)"])]
		print(indic_data["Indicator"])
	except:
		print("no data found for: " + file)
