# -*- coding: utf-8 -*-
"""
Created on Fri May 28 16:41:19 2021

@author: Akshay Prakash
"""

import math
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv(r'C:\Users\Akshay Prakash\Downloads\96-20PL.csv')
# data = {'x': [1, 2 ,3, 4, 5, 6, 7, 8, 9, 10], 'y': [10,12,16,28,25,36,41,49,40,50]}
df1 = pd.read_csv(r'C:\Users\Akshay Prakash\Downloads\F2021PL.csv')

df.head()
n = (len(df))

mean_x = sum(df['Rk'])/n
#print("Mean of x is:", mean_x)

mean_y = sum(df['Pts'])/ n 
#print("Mean of y is:", mean_y)

xy = []
m= 0
for i in df['Rk']:
    xy.append(df.iloc[m]['Rk'] * df.iloc[m]['Rk'])
    m += 1
    
#If you give it 0 it will [10,10,10,10], hence m = 0 and m + 1
#initialise empty list so you can apppend and store values in it
#print(xy)
df['xy']= xy

x_2 = []
m = 0
for i in df['Rk']:
    x_2.append(df.iloc[m]['Rk'] * df.iloc[m]['Rk'])
    m +=1

df['x_2'] = x_2

Totalx_2 = sum(x_2)

sd_x2 = (Totalx_2/n) - mean_x * mean_x
sd_x = (sd_x2 **0.5)


y_2 = []
m = 0
for i in (df['Pts']):
    y_2.append(df.iloc[m]['Pts'] * df.iloc[m]['Pts'])
    m+=1
df['y_2']= y_2
Totaly_2 = sum(df['y_2'])

sd_y2 = (Totaly_2/n)- mean_y * mean_y

sd_y = (sd_y2 **0.5)

z = []
m = 0
for i in (df['Pts']):
    z.append(df.iloc[m]['Rk'] - df.iloc[m]['Pts'])
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
#print(y_pred)

y_pred1 = []
m = 0
for i in df['Rk']:
    y_pred1.append(float(df.iloc[m]['Pts'] - intercept)/slope)
    m +=1

#df['y_new'] = y_pred1
print(df)
y_plot = df.Rk
x_plot = df.Pts.values.reshape(-1,1)
#yplot = df.y_new
#print(x_plot.shape, yplot.shape)
#print(x_plot.shape, y_plot.shape)

y2021 = df1.Rk
x2021 = df1.Pts.values.reshape(-1,1)



fig, ax = plt.subplots(figsize = (10,12))
plt.scatter(x_plot, y_plot)
#plt.scatter(x_plot, y_pred1)


plt.plot(x_plot, y_pred1, color = 'red', label = 'Regression line')
plt.plot(x2021, y2021, color = 'blue')

plt.ylim(0.5, 20.5) #dont do 0 because there's no 0 position
plt.yticks([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]) 
plt.gca().invert_yaxis()#rewrite because it should be from low to high
plt.xlabel('Points')
plt.ylabel('League Position (Rank)')
plt.title('Evaluating relationship between Points and league position (EPL)')

plt.text(8, 4.7, "Model based on using Points from seasons 2003-04/08-09\nto predict Points of 2009-10", color = '#53162f', size = '10')
plt.text(8, 5.5, f'Slope: {slope}', color = 'red', size= '10')
plt.text(8, 6.1, f'Intercept: {intercept}', color = 'red', size= '10')
plt.text(8, 6.7, f'r_sqrt (Accuracy): {r}', color = 'red', size= '10')


plt.text(80, 20, "Twitter: @aprakash_7", color = '#5CBFEB', size = '10')
plt.text(84, 18.8, "Stats via fbref", fontname= 'Franklin Gothic Medium', color = 'black', size = '13')
#'Impact' 

plt.text(88, 1.4, "Chelsea 04/05 (95)", color ='red', size = '7')
plt.text(7, 19.4, "Derby County 08/09 (11) ", color = 'red', size= '7')

annotations = df1['Pts'].to_list()
annotations = tuple(annotations)
print(annotations)

for i, label in enumerate(annotations):
   plt.text(x2021[i],y2021[i], label, color = '#53162f', size = '14')

def predpoints(y_10):        
    #y_2 = int(input("Enter a number: "))
    x_10 = float(slope * y_10 + intercept)
    print("The predicted points for your rank is" , x_10)
y_rank = 0

while True: 
    print("_____________________________________________________________________________")
    print("\n\nThis is a model to predict the Points of League positions in the English")
    print("Premier League for season 2009/10 based on data from seasons 2003-04/ 2008-09\n")
    print("\nWelcome to Main Menu!")
    print("\n1. Predict the Points of your team in a league position")
    print("2. List of all the predicted points for season 2009/10")
    print("3. Actual Table for season 2009/10")
    print("4. Exit to see the plot! ")
    print("\n\n_____________________________________________________________________________")
    choice = int(input("Enter your choice: "))
    
    if choice ==1:
        y_10 = int(input("Enter the league position you want to predict: "))
        if 0<y_10<20:
            predpoints(y_10)
        else: 
            print("Invalid position")
    
    elif choice ==2:
        for y_new in range(1,21):
            y_rank += 1
           
            x1 = slope * y_new + intercept
            print("\nHere's your list:", y_rank)
            print(x1)
        
         # for y_new in range(1,21):
         #    x1 = (y_new - intercept)/slope
         #    print(x1)
            
    elif choice ==3:
        df = pd.read_csv(r'C:\Users\Akshay Prakash\Downloads\F2021PL.csv')
        print(df)
        print("\n\n")
    
    elif choice ==4:
        break
    else:  
        print("Invalid choice")


plt.grid()
plt.show()