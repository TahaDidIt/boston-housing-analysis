# -*- coding: utf-8 -*-
"""
Created on Sun Apr  7 12:25:26 2024

@author: Taha
"""
##### SET-UP
from datetime import datetime
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats
import statsmodels.api as sm
from statsmodels.formula.api import ols
from scipy.stats import norm


#Loading Boston dataset into a pandas dataframe
csvPathBoston = "C:/Taha/projects/Data Science Fundamentals with Python and SQL/Working directory/boston.csv"
bostonData = pd.read_csv(csvPathBoston)
print(bostonData.describe())





##### PROJECT - BOSTON DATASET (Kaggle bookmarked)

"""TASKS:
    Is there a significant difference in the median value of houses
    bounded by the Charles river or not? [DONE]

    Is there a difference in median values of houses of each proportion
    of owner-occupied units built before 1940?

    Can we conclude that there is no relationship between
    Nitric oxide concentrations and the proportion of non-retail business acres
    per town?

    What is the impact of an additional weighted distance to the 
    five Boston employment centres on the median value of owner-occupied homes?

"""

#A general OLS regression fitting all variables
def generalReg():
    pass


#An OLS regression fitting CHAS (river dummy variable)
def medvRiverReg():
    #Set up variables and add intercept property
    X = bostonData["CHAS"].astype(int)
    X = sm.add_constant(X)
    y = bostonData["MEDV"]
    
    #Create and fit model, create model predicitons
    model = sm.OLS(y, X).fit()
    modelPred = model.predict(X)
    
    print(model.summary)
    print("")
    print(modelPred)


def medvRiverVis():
    """ making: Avg medv when bound or not, with bar chart. box plot"""
    #Gives ALL entries where CHAS=1 into seperate datasets
    housesBound = bostonData[bostonData["CHAS"] == 1]
    #Take JUTS the Medv variable and CHAS
    housesBound = housesBound[["MEDV", "CHAS"]]
    #Vice versa for CHAS=0
    housesNotBound = bostonData[bostonData["CHAS"] == 0]
    housesNotBound = housesNotBound[["MEDV", "CHAS"]]
    
    #Print averages
    print("Average Medv for houses that are Not Bound: {0}; Bound: {1}".format(
        housesNotBound["MEDV"].mean(), housesBound["MEDV"].mean()))
    
    #Barplot
    #put them into 1 dataframe of the AVERAGE Medv first
    housesAvgMedv = pd.DataFrame([housesNotBound["MEDV"].mean(),
                                  housesBound["MEDV"].mean()])
    ax = housesAvgMedv.plot(kind = "bar", figsize = (3, 6))
    ax.set_ylabel("Average MEDV")
    ax.set_xlabel("Houses bound by Charles river")
    plt.show()
    
    #Boxplot
    #concat dataset together
    housesMedvSpread = pd.concat([housesNotBound, housesBound])
    #Remap CHAS as it wasnt working perfectly with 1s and 0s, nor True & False
    housesMedvSpread["CHAS"] = housesMedvSpread["CHAS"].replace({0: "Not Bound", 1: "Bound"})
    ax = sns.boxplot(x = "MEDV", y = "CHAS", data = housesMedvSpread)
    plt.show()


def medvRiverTTest():
    #Seperate Medv valeus into 2 groups based on CHAS
    medvChas0 = bostonData[bostonData["CHAS"] == 0]["MEDV"]
    medvChas1 = bostonData[bostonData["CHAS"] == 1]["MEDV"]
    
    #T-test
    tStat, pValue = scipy.stats.ttest_ind(medvChas0, medvChas1)
    print("t-statistic: ", tStat)
    print("P-value: ", pValue)





##### MAIN MENU

### Visualisations index
plotFunctions = {1: generalReg, 2: medvRiverReg, 3: medvRiverVis,
                 4: medvRiverTTest}

### Menu
menuChoice = ""

while menuChoice != "0":
    #Time and spacer for ease of reading
    print("")
    print("")
    print("")
    print("########## ", "Current Time: ", datetime.now().strftime("%H:%M:%S"))
    print("")
    #Menu choices
    print("Main Menu:")
    for i in plotFunctions:
        print(i, ": ", plotFunctions[i])
    
    menuChoice = input("Please select a number from the options: ")
    if menuChoice == "0":
        pass
    elif int(menuChoice) in plotFunctions:
        print("")
        plotFunctions[int(menuChoice)]()
    else:
        print("Invalid choice, please try again.")