# -*- coding: utf-8 -*-
"""
Created on Wed May 26 12:54:53 2021

@author: Akshay Prakash
"""

import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression 
from Regression import result1

#sklearn -machine learning library; consists of linear_model; consists of class Linear Regression
#From Regression.py import Result1 variable

#print(result1['Pts'])
y = result1.Rk
x = result1.Pts.values.reshape(-1,1)
#reshape x so it become a 1 row 1 column 

#print(x.shape, y.shape)
lin = LinearRegression()
#Linear Regression() is a class which is gonna be assigned to lin here

model = lin.fit(x, y)
#Model is an instance of class linear regression here, which now fits x and y in the 
#form of linear regression

#Create model instance and pass in Linear Regression

r_sqrt = model.score(x,y)
#Calculates r*2

#print("r_sqrt: ", r_sqrt)

intercept = model.intercept_ #Calculates intercept 
slope = model.coef_ #Calculatees slope

#print('intercept: ', intercept)
#print('slope: ', slope)

y_predicted = model.predict(x)
#y_predicted = intercept + slope* x #Linear Regression eqn
     
df = pd.read_csv(r'C:\Users\Akshay Prakash\Downloads\F0910PL.csv')
#You can add any Actual dataframe that you're trying to predict     
#(df['Pts'])

y3 = df.Rk
x3 = df.Pts.values.reshape(-1,1)
#This mentions your x and y axis. This case, x3 and y3. You can check it out by printing x3 and y3
#To get rows and columns, use (x.shape, y.shape)


#mean = sum(average_line)/20
#mean is 52.07

#Make new function predpoints and add a formula of your choice! Don't forget to call it.
def predpoints(y_2):        
    x_2 = (y_2- intercept)/slope
    print("The predicted points is:", x_2)

y_rank = 0

x_predictedd= []
m = 0
for i in df['Rk']:
    x_predictedd.append((df.iloc[m]['Rk']- intercept)/slope)
    m+= 1
df['Predicted Points']= x_predictedd

#Menu Driven Program
while True: 
    print("\n\nThis is a model to predict the Points of League positions in the English")
    print("Premier League for season 2009/10 based on data from seasons 2008/09\n")
    print("\nWelcome to Main Menu\n")
    print("\n1. Predict the Points of your team in a league position")
    print("2. List of all the predicted points for season 2009/10")
    print("3. Actual Table for season 2009/10")
    print("4. See plot! ")
    print("5. Exit")
    choice = int(input("Enter your choice: "))
    
    if choice ==1:
        y_2 = int(input("Enter a league position: "))
        if 0<y_2<20:
            predpoints(y_2) #Call the function, the formula exists in this function
        else: 
            print("Invalid position")
    
    elif choice ==2:
        for y_new in range(1,21):
            y_rank += 1
            x1 = (y_new- intercept)/slope
            print("\nHere's your rank:", y_rank)
            print(x1)
        #For loop to give the list of predictions 
        
    elif choice ==3:
        df = pd.read_csv(r'C:\Users\Akshay Prakash\Downloads\F0910PL.csv')
        print(df)
        print("\n\n")
        #Returns The Data Frame of season 2008-09
    elif choice == 4:
        fig, ax = plt.subplots(figsize = (15, 10))
        #Make sure to use this while demonstrating (15,10)

        plt.scatter(x,y, color = 'blue', label = 'Points Over the years 2003-04/2008-09')
        #Plots x and y 

        plt.scatter(x3,y3, color = 'orange', label = 'Actual Points Of 2009/10')
            #plt.scatter(avg_x,avg_y, color = '#5CBFEB', label = 'Average Points of the position')

        plt.grid(color = 'skyblue', lw= 0.5, ls= '--')
        plt.plot(x,y_predicted, color = 'red', label = 'Regression Line (Predicted Points)')
        #Plot Regression line 

        plt.plot(x3,y3, color = 'black', label = 'Actual Result of 2009/10')
        #Plot Actual result 
        #Two graphs are displayed which means that for 3 plots, there'll be three plots shown

        plt.plot([df['Pts'].mean(), df['Pts'].mean()], [1,20], 'k-', linestyle = ':', lw=1, color = '#EF0107', label = 'Mean')
        #Plots mean 
        plt.plot([19,19], [20,21], 'k--', lw = 0.5, color = 'black')# To show result 
        #Add this line to show that Linear Regression is better than just taking average
        #plt.plot([20,90], [df['Pts'].mean(), df['Pts'].mean()], 'k-', linestyle = ':', lw=1)


        plt.legend()
        plt.ylim(0.5, 20.5) #dont do 0 because there's no 0 position

        plt.yticks([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]) 
        plt.gca().invert_yaxis()#rewrite because it should be from low to high
        #Invert the axis using .gca().invert_yaxis()
        #Hence graph is inverted and intercept is showing otherwise 

        plt.xlabel('Points')
        plt.ylabel('League Position (Rank)')
        plt.title('Evaluating relationship between Points and league position (EPL)')

        plt.text(8, 4.4, "Model based on Points from 2003/04 -08/09", color = '#53162f', size = '11')
        plt.text(8, 5.1, f'Slope: {slope}', color = 'red', size= '10')
        plt.text(8, 5.8, f'Intercept: {intercept}', color = 'red', size= '10')
        plt.text(8, 6.5, f'r (Accuracy): {r_sqrt}', color = 'red', size= '10')


        plt.text(80, 20, "Twitter: @aprakash_7", color = '#5CBFEB', size = '10')
        #Add this if you want to 

        # plt.text(80, 16, "Games Played: 38", color = 'red', size = '10')
        # plt.text(80, 16.7, "Points per Win: +3", color = 'red', size = '10')
        # plt.text(80, 17.4, "Points per Draw: +1", color = 'red', size = '10')
        # plt.text(80, 18.1, "Points per Loss: 0", color = 'red', size = '10')
        plt.text(84, 18.8, "Stats via fbref", fontname= 'Franklin Gothic Medium', color = 'black', size = '13')
        #'Impact' 


        plt.text(88, 1.4, "Chelsea 04/05 (95)", color ='red', size = '7')
        plt.text(7, 19.4, "Derby County 08/09 (11) ", color = 'red', size= '7')

        annotations = df['Pts'].to_list() #Convert array to list and then to tuple
        annotations = tuple(annotations)
        #print(annotations)

        for i, label in enumerate(annotations):
            plt.text(x3[i],y3[i], label, color = '#53162f', size = '14')
            #The Python Enumerate() command adds a counter to each item of 
            #the iterable object and returns an enumerate object as an output string.
            #That is the reason we have converted annotations to tuple, so it can iterate
        
        plt.show()
    elif choice ==5:
        break
    
    else:  
        print("Invalid choice")

