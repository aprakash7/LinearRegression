# -*- coding: utf-8 -*-
"""
Created on Tue May 25 01:23:03 2021

@author: Akshay Prakash
"""

import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression 
from Regression import result1
print(result1['Pts'])
y = result1.Rk
x = result1.Pts.values.reshape(-1,1)
print(x.shape, y.shape)

model = LinearRegression().fit(x, y)
r_sqrt = model.score(x,y)
print("r_sqrt: ", r_sqrt)
intercept = model.intercept_
slope = model.coef_
print('intercept: ', intercept)
print('slope: ', slope)

y_predicted = intercept + slope* x #Linear Regression eqn

for y_new in range(1,21):
    x1 = (y_new- intercept)/slope
    print(x1)
        
y_2 = int(input("Enter a number: "))
x_2 = (y_2- intercept)/slope
print(x_2)


df = pd.read_csv(r'C:\Users\Akshay Prakash\Downloads\F0910PL.csv')
#print(df)
(df['Pts'])
y3 = df.Rk
x3 = df.Pts.values.reshape(-1,1)

#average_line = (90.3, 83.16, 78.0, 67.33,     61.16, 59.5, 55.5, 54.0, 53.16,49.83,47.5,45.66,43.66,
                #42.83,41.66,39,36.66,34,66,32.83,25.16) 
#avgdf = pd.DataFrame({'Rk':[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20], 
                      #'Pts': [90, 83, 78, 67, 61, 60, 56, 54, 53, 50, 48, 46, 44, 43, 42, 39, 37, 35, 33, 25]})
#print(avgdf)
#avg_y= avgdf.Rk
#avg_x = avgdf.Pts.values.reshape(-1,1)

fig, ax = plt.subplots(figsize = (10,10))
plt.scatter(x,y, color = 'blue', label = 'Points')
plt.scatter(x3,y3, color = 'orange', label = 'FinalPoints Of 2009/10')
#plt.scatter(avg_x,avg_y, color = '#5CBFEB', label = 'Average Points of the position')


plt.plot(x,y_predicted, color = 'red', label = 'Regression Line (Predicted)')
plt.plot(x3,y3, color = 'black', label = 'Final Result of 2009/10')
plt.plot([df['Pts'].mean(), df['Pts'].mean()], [1,20], 'k-', linestyle = ':', lw=1, color = '#EF0107', label = 'Mean')
#Add this line to show that Linear Regression is better than just taking average

#plt.plot([20,90], [df['Pts'].mean(), df['Pts'].mean()], 'k-', linestyle = ':', lw=1)

plt.legend()
plt.ylim(0.5, 20.5) #dont do 0 because there's no 0 position
plt.yticks([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]) 
plt.gca().invert_yaxis()#rewrite because it should be from low to high
plt.xlabel('Points')
plt.ylabel('League Position (Rank)')
plt.title('Evaluating relationship between Points and league position')

plt.text(8, 4, "Model based on Points from 2003/04 -09/10", color = '#53162f', size = '12')
plt.text(8, 4.7, f'Slope: {slope}', color = 'red', size= '10')
plt.text(8, 5.4, f'Intercept: {intercept}', color = 'red', size= '10')
plt.text(8, 6.1, f'r_sqrt (Accuracy): {r_sqrt}', color = 'red', size= '10')
plt.text(82, 20, "Akshay Prakash", color = '#5CBFEB', size = '12')

plt.text(88, 1.4, "Chelsea 04/05 (95)", color ='red', size = '7')
plt.text(7, 19.6, "Derby County 08/09 (11) ", color = 'red', size= '7')

annotations = df['Pts'].to_list()
annotations = tuple(annotations)
print(annotations)

for i, label in enumerate(annotations):
   plt.text(x3[i],y3[i], label, color = '#53162f', size = '14')
#The Python Enumerate() command adds a counter to each item of 
#the iterable object and returns an enumerate object as an output string.

#mean = sum(average_line)/20
#mean is 52.07



