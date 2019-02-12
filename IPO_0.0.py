# -*- coding: utf-8 -*-
"""
Created on Fri Oct 12 12:13:36 2018
numero reservation/jour/heure/depart/arrivée/course annulée/prix brut (HT)/TVA/prix brut (TTC)/Commission Kolett/

en haut total 
nom du chauffeur
date debut 
date fin

@author: Olivier
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


source = 'C:\\Users\\Olivier\\Documents\\Recherche\\DataSets\\Merger\\ipo_ue_1.xlsx'
#output= 'C:\\Users\\Olivier\\Documents\\Kolett\\BookingDetails_Sortie.xlsx'
df=pd.read_excel(source, index = False)

#♥date
df['Announce Date'] =pd.to_datetime(df['Announce Date'])
df=df.sort_values(by='Announce Date')


#data cleaning
df['Target Ticker'].unique()
len(df['Target Ticker'].notnull().unique())
df['Target Ticker'][df['Target Ticker'].notnull()]
len(df['Target Ticker'][df['Target Ticker'].notnull()].unique())

#tous les target ayant un ticker
#ceux n appartenant sont des deals privés
df_noprivate=df[df['Target Ticker'].notnull()]

#we want to exclude the non listed deals 
#those are with numerics
#we must have taken out the NaN, ie df_noprivate
df_noprivate['Target Ticker 2']=df_noprivate['Target Ticker'].str[:3].str.isnumeric().astype('uint8')
df_noprivate_noliste=df_noprivate[df_noprivate['Target Ticker 2']!=1]

#on peut faire qq checks sur les repartitions des deals

#on a besoin d identifier les deals faisant l objet d un contre bid
#creation d 'une variable booleenne si target ticker apparait dans les 90 jours precedant

for i in range(len(df_noprivate_noliste)-120):
    if df_noprivate_noliste['Target Ticker'].iloc[i] in set(df_noprivate_noliste['Target Ticker'].iloc[i+1:i+90]):
        df_noprivate_noliste['Counterbid']=1
    else:
        df_noprivate_noliste['Counterbid']=0

##demander a Alain

#on degage les colonnes
#'Dispatch #','ID#/ National IC#',,'Driver license number'
"""
col_todrop=['Booking service','Service Type','Driver license number',
            'Basic fare calculator(€)','Basic fare(€)','Surcharge(€)','Operator',
            'Passenger phone number','Passenger name','Division','Dept','Queuing area',
            'Dispatch time','Pickup location lat/long','Actual destination lat/long', 'Notes',
            'Old basic fare(€)','Airport fee(€)', 'Meet driver(€)','Tech fee(€)', 'Promo amt(€)']

df=df.drop(['Booking service','Service Type','Driver license number',
            'Basic fare calculator(€)','Basic fare(€)','Surcharge(€)','Operator',
            'Passenger phone number','Passenger name','Division','Dept','Queuing area',
            'Dispatch time','Pickup location lat/long','Actual destination lat/long',
            'Notes', 'Old basic fare(€)','Airport fee(€)', 'Meet driver(€)',
            'Dispatch #','Promo code','ID#/ National IC#','Tech fee(€)', 'Promo amt(€)'], 
            axis=1)
"""
"""
#evolution du nombre de courses
print(plt.hist(df_course_real['Jour']))
print(plt.hist(df_course_real['Jour de la semaine']))
print(plt.hist(df_course_real['Commission Kolett']))

#scatter jour heure
print(plt.hist(df_course_real['Jour']))
print(plt.hist(df_course_real['Heure']))
plt.scatter(df_course_real['Jour de la semaine'],df_course_real['Heure'],color='r')
plt.title('course real: jour vs heure')
plt.xlabel('Jour de la semaine')
plt.ylabel('Heure')
plt.xlim(0,6)
plt.ylim(0, 24)
print(plt.show())



#print(plt.hist(df_course_cancelled['Jour']))
#print(plt.hist(df_course_cancelled['Heure']))
plt.scatter(df_course_cancelled['Jour de la semaine'],df_course_cancelled['Heure'],color='g')
plt.title('course cancel: jour vs heure')
plt.xlabel('Jour de la semaine')
plt.ylabel('Heure')
plt.xlim(0,6)
plt.ylim(0, 24)

plt.scatter(df_course_real['Jour de la semaine'],df_course_real['Heure'],color='r')
plt.title('course real: jour vs heure')
plt.xlabel('Jour de la semaine')
plt.ylabel('Heure')
plt.xlim(0,6)
plt.ylim(0, 24)

"""

print(plt.show())



#unique driver
list_unique_driver=df2['Driver name'].unique()
print(df2['Driver name'])

#•checke for 1 driver
df_driver=[0]
df_driver=df2[df2['Driver name']==df2['Driver name'][0]]

#formating
df_driver.style.format("{:.2%}")
print(df_driver)

#df_driver.to_excel(output,df2['Driver name'][0], index = False)
#df_driver.to_html(output,df2['Driver name'][0], index = False)
os.startfile(output)