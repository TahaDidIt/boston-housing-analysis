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
    bounded by the Charles river or not?

    Is there a difference in median values of houses of each proportion
    of owner-occupied units built before 1940?

    Can we conclude that there is no relationship between
    Nitric oxide concentrations and the proportion of non-retail business acres
    per town?

    What is the impact of an additional weighted distance to the 
    five Boston employment centres on the median value of owner-occupied homes?

"""







##### MAIN MENU

### Visualisations index
plotFunctions = {}


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