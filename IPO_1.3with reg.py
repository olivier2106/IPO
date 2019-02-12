# -*- coding: utf-8 -*-
"""
Created on Wed Jan 31 22:17:04 2018

@author: Olivier

pour calculer si hot
il faut rajouter la perf des jours avant pour 

pour nb de deals per day
il faut savoir compter

"""

#librairies
import numpy as np
import pandas as pd
import os
import openpyxl
import matplotlib.pyplot as plt
import statsmodels.api as sm
from scipy import stats
from sklearn.linear_model import LinearRegression

source='C:\\Users\\Olivier\\Documents\\Doc Perso\\Axes de recherche\\IPO\\IPO_DATA.xlsx'
#import excel
df=pd.read_excel(source)

def remove_unnamed_cols(df):
    df=df[[col for col in df.columns if 'Unnamed:' not in col]]
    return df
df=remove_unnamed_cols(df)


#creation des df de marqueurs
df["year"]= df["First Trade Date"].dt.year
df["month"]= df["First Trade Date"].dt.month
df["day"]= df["First Trade Date"].dt.day
df["day of the week"]= df["First Trade Date"].dt.dayofweek


#df["IPO on Day"]= df.groupby(df["First Trade Date"]).count()
df["IPO on Day"]=df.groupby(df["First Trade Date"]).count()

def nb_ipo_on_day_df():
    ligne_start=1
    n=len(df["First Trade Date])
    vect=[1]*n
    for k in range(ligne_start+1,n+ligne_start):
        if (df["First Trade Date"][k] == df["First Trade Date"][k-1]):
            vect[k]=1+
    return vect

#split the bookrunner list in different columns
df['BR1'], df['BR2'], df['BR3'] = df["Deal Bookrunner Parent"].str.split(';', 2).str

#split the exchange list in different columns if several
df['Exc1'], df['Exc2'], df['Exc3'] = df["Exchange Nationality"].str.split(';', 2).str

#split the shareholders list in different columns
df['SS1'], df['SS2'], df['SS3'], df['SS4'] = df["Selling Shareholder"].str.split(';', 3).str

#split in bucket the percentage sold
df['Home']= df["Exchange Nationality"] == df["Issuer Nationality"] 
df["play home"]=df['Home']*df["% Change Price Offer/Open"]

#split in bucket the percentage sold
df["Bucket % Sold"] = pd.qcut(df["% of Company Sold"], 20, labels=False)

#split in bucket the percentage sold
df["Bucket % Mkt Value"] = pd.qcut(df["Market Value (Euro)"], 20, labels=False)

#split in bucket the percentage sold
#df["Bucket % Offer Price"] = pd.qcut(df["Offer Price"], 10, labels=False)

#split in bucket the percentage sold
df["Width Range"] = (-df["Current Range Low"] +df["Current Range High"] )/df["Current Mid Point Range"] 
#df["Bucket Width Range"] =pd.qcut(df.dropna(subset = ["Width Range"]), 10, labels=False)

#split in bucket the percentage sold
df["Intraday move day1"] = (-df["% Change Price Offer/Open"] +df["% Change Price Offer/1 Day"] )

#split in bucket the percentage sold
df["Road Show Length"] = (df["Pricing Date"] -df["Announcement Date"])

#split in bucket the percentage soldd
df["Time from Price to Market"] = (df["First Trade Date"] -df["Pricing Date"] )

#split in bucket the percentage soldd
df["Perf 12 -1 M"] = (df["% Change Price Offer/1 Yr"] -df["% Change Price Offer/1 Month"] )
df["Negative Perf 1D"] = df["% Change Price Offer/1 Day"]<0
df["Perf 12 -1 M if 1d neg"]=df["Negative Perf 1D"]*df["Perf 12 -1 M"]
df["Very Positive Perf 1D"] = df["% Change Price Offer/1 Day"] > 6
df["Perf 12 -1 M if Very Positive Perf 1D"]=df["Very Positive Perf 1D"]*df["Perf 12 -1 M"]
#print(df["Perf 12 -1 M if 1d neg"].mean)

#df["Bucket Perf 12 -1 M"] =pd.qcut(df.dropna(subset = ["Perf 12 -1 M"]), 10, labels=False)
#df["Bucket Intraday move day1"] = pd.qcut(df["Intraday move day1"], 20, labels=False)
#print (df["Bucket Intraday move day1"])

#plt.hist(df[], normed=True, bins=30)
df.hist(column="Perf 12 -1 M", bins=20)
plt.title("Carry Out Distribution")
plt.xlabel("Value")
plt.ylabel("Probability")
plt.show()

"""
#df['% Change Price Offer/1 Day'])=df.target
X = df["Intraday move day1"].values
y = df["% Change Price Offer/Open"].values
 

# Note the difference in argument o
model =sm.OLS(y, X)
model = model.fit() # make the predictions by the model

# Print out the statistics
model.summary()

"""
output='C:\\Users\\Olivier\\Documents\\Doc Perso\\Axes de recherche\\IPO\\IPO_DATA_Ouput.xlsx'
df.to_excel(output)
os.startfile(output)
