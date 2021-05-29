# -*- coding: utf-8 -*-
"""
Created on Fri May 28 14:02:46 2021

@author: Akshay Prakash
"""

import math
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt 

data = {'x': [1, 2 ,3, 4, 5, 6, 7, 8, 9, 10], 'y': [10,12,16,28,25,36,41,49,40,50]}
df = pd.DataFrame(data)
df.head()
n = (len(df))

mean_x = sum(df['x'])/n
print("Mean of x is:", mean_x)

mean_y = sum(df['y'])/ n 
print("Mean of y is:", mean_y)

xy = []
m= 0
for i in df['x']:
    xy.append(df.iloc[m]['x'] * df.iloc[m]['y'])
    m += 1
    
#If you give it 0 it will [10,10,10,10], hence m = 0 and m + 1
#initialise empty list so you can apppend and store values in it
print(xy)
df['xy']= xy

x_2 = []
m = 0
for i in df['x']:
    x_2.append(df.iloc[m]['x'] * df.iloc[m]['x'])
    m +=1

df['x_2'] = x_2

Totalx_2 = sum(x_2)

sd_x2 = (Totalx_2/n) - mean_x * mean_x
sd_x = (sd_x2 **0.5)


y_2 = []
m = 0
for i in (df['y']):
    y_2.append(df.iloc[m]['y'] * df.iloc[m]['y'])
    m+=1
df['y_2']= y_2
Totaly_2 = sum(df['y_2'])

sd_y2 = (Totaly_2/n)- mean_y * mean_y

sd_y = (sd_y2 **0.5)

z = []
m = 0
for i in (df['y']):
    z.append(df.iloc[m]['x'] - df.iloc[m]['y'])
    m+= 1


df['z']= z
Totalz = sum(df['z'])
mean_z = Totalz/n

z_2 = []
m = 0
for i in (df['z']):
    z_2.append(df.iloc[m]['z'] * df.iloc[m]['z'])
    m+=1
    
df['z_2'] = z_2
Totalz_2= sum(df['z_2'])

Totalz_2 = sum(df['z_2'])
sd_z2= (Totalz_2/ n) - mean_z * mean_z
sd_z = (sd_z2 ** 0.5)

r = float(sd_x2 + sd_y2 - sd_z2)/  float(sd_x * sd_y*2)
#Use float here, otherwise you'll get 1150.98 thinking where you went wrong in life xD 

slope = (r* (sd_y/sd_x))
print(slope)

intercept= mean_y - (r* (sd_y/sd_x)* mean_x)
print(intercept)

x_new = int(input("Enter a number: "))
y_pred = (slope * x_new + intercept)
print(y_pred)

y_pred1 = []
m = 0
for i in df['x']:
    y_pred1.append(slope * df.iloc[m]['x'] + intercept)
    m +=1

print(y_pred1)
df['y_new'] = y_pred1
y_plot = df.y
x_plot = df.x.values.reshape(-1,1)

print(x_plot.shape, y_plot.shape)

fig, ax = plt.subplots(figsize = (10,12))
plt.scatter(x_plot, y_plot)
plt.plot(x_plot, y_pred1, color = 'red', label = 'Regression line')
plt.grid()