# -*- coding: utf-8 -*-
"""
y a t il correlation entre les downsize upsize _cree une variable time series_
la dispersion des predictions est elle informative _cree une variable_
avec le nb d event durant dernier mois ou quarter _cree une variable_

"""
import os
import openpyxl
import matplotlib.pyplot as plt
import statsmodels.api as sm
from scipy import stats
from sklearn.linear_model import LinearRegression
from os.path import expanduser as ospath
import datetime as dt
import numpy as np
import pandas as pd
import scipy.stats as stats
import geoplotlib
import pyglet


source = 'C:\\Users\\Olivier\\Documents\\Recherche\\DataSets\\Corporate Actions\\IPO_Europe.xlsx'
#output= 'C:\\Users\\Olivier\\Documents\\Kolett\\BookingDetails_Sortie.xlsx'
df=pd.read_excel(source, index = False)


##remove unuseful
#exclude non trading
df=df[df['Offer Stage']=='Trading']
#remove non important columns
df=df.drop(['Action Id','Action Type'],axis=1)

#sort
df=df.sort_values(by='Announced Date')

##variable creation
#country
df['Country']=df['Issuer Ticker'].str[-2:]

#♥date
df['Announced Date'] =pd.to_datetime(df['Announced Date'])
df['Announced Date'] = pd.to_datetime(df['Announced Date'], infer_datetime_format=True)
df['Année']=df['Announced Date'].dt.year
df['Month']=df['Announced Date'].dt.month
df['Week']=df['Announced Date'].dt.week
df['Jour']=df['Announced Date'].dt.day
df['Jour de la semaine']=df['Announced Date'].dt.dayofweek
df['Pricing Date']=pd.to_datetime(df['Pricing Date'], infer_datetime_format=True)
df['Time to price']=((df['Pricing Date']-df['Announced Date']).fillna(0)/np.timedelta64(1,'D')).astype(int)


#nb ipo on the day
df['nb Ipo on day']=(df.groupby('Pricing Date')['Pricing Date'].transform('size'))
df['Ipo on day']=((df['nb Ipo on day'].fillna(0))).values.astype(int)

#evolution du nombre d ipo
(plt.hist(df['Jour']))
(plt.hist(df['Jour de la semaine']))
(plt.hist(df['Month']))
(plt.hist(df['Année']))

#encoding of df['Up/Down Sized']
df['Sized']=np.where(df['Up/Down Sized']=='Upsized',1,np.where(df['Up/Down Sized']=='Downsized',-1,0))

plt.hist(df['Année'][df['Sized']==1])
plt.hist(df['Année'][df['Sized']==-1])

#quantile Offer Size (M)
df['Offer Size Decile']=pd.qcut(df['Offer Size (M)'],10,labels=False)

df.pivot_table(index='Offer Size Decile', columns='Sized', aggfunc='Offer To 1st Open', fill_value=0)

df.pivot_table(values='Offer To 1st Open', index=['Sized'],columns=['Security Type'], aggfunc=np.mean)


#print(plt.hist(df_course_cancelled['Jour']))
#print(plt.hist(df_course_cancelled['Heure']))
plt.scatter(df['Jour de la semaine'],df['Sized'],color='g')
plt.title('course cancel: jour vs upsized')
plt.xlabel('Jour de la semaine')
plt.ylabel('upsize')

df.pivot_table(index='Jour de la semaine', columns='Sized', aggfunc='Offer To 1st Open', fill_value=0)


#df_driver.to_excel(output,df2['Driver name'][0], index = False)
#df_driver.to_html(output,df2['Driver name'][0], index = False)
os.startfile(output)