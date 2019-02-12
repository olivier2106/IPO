# -*- coding: utf-8 -*-
"""
Created on Wed Jan 31 22:17:04 2018

@author: Olivier
"""

#librairies
import numpy as np
import pandas as pd
import os
import openpyxl
import matplotlib.pyplot as plt

source='C:\\Users\\Olivier\\Documents\\Doc Perso\\Axes de recherche\\IPO\\IPO_DATA.xlsx'
#import excel
df=pd.read_excel(source)

def remove_unnamed_cols(df):
    df=df[[col for col in df.columns if 'Unnamed:' not in col]]
    return df
df=remove_unnamed_cols(df)
'''
temp=df["Deal Bookrunner Parent"].split(";")
print (temp)
'''

#split the bookrunner list in different columns
df['BR1'], df['BR2'], df['BR3'] = df["Deal Bookrunner Parent"].str.split(';', 2).str

#split the exchange list in different columns if several
df['Exc1'], df['Exc2'], df['Exc3'] = df["Exchange Nationality"].str.split(';', 2).str

#split the shareholders list in different columns
df['SS1'], df['SS2'], df['SS3'], df['SS4'] = df["Selling Shareholder"].str.split(';', 3).str

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
df["Road Show Length"] = (-df["Announcement Date"] +df["Pricing Date"] )

#split in bucket the percentage sold
df["Price to Market"] = (df["First Trade Date"] -df["Pricing Date"] )

#df["Bucket Intraday move day1"] = pd.qcut(df["Intraday move day1"], 20, labels=False)
#print (df["Bucket Intraday move day1"])

#plt.hist(df[], normed=True, bins=30)
df.hist(column='Intraday move day1', bins=20)
plt.title("Carry Out Distribution")
plt.xlabel("Value")
plt.ylabel("Probability")
plt.show()


output='C:\\Users\\Olivier\\Documents\\Doc Perso\\Axes de recherche\\IPO\\IPO_DATA_Ouput.xlsx'
df.to_excel(output)
os.startfile(output)
