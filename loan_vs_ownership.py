'''
Created on Sep. 4, 2019

@author: Zhe Fan
'''
#the following packages will be used to help us extract data from csv files, and manipulate them into dataframes
import numpy as np

import pandas as pd

import matplotlib.pyplot as plt

import jinja2 as jj

#initialize two dataframes using the loan_data.csv file and the home_ownership.csv file
loan_data = pd.read_csv('loan_data.csv', delimiter = ',')

home_ownership_data = pd.read_csv('home_ownership_data.csv', delimiter = ',')
#Generate three pandas series of member_ids for each home_ownership type
MORTGAGE_OWNERS = home_ownership_data.loc[(home_ownership_data["home_ownership"]=="MORTGAGE"), ["member_id"]]
RENT_OWNERS = home_ownership_data.loc[(home_ownership_data["home_ownership"]=="RENT"),["member_id"]]
OWN_OWNERS = home_ownership_data.loc[(home_ownership_data["home_ownership"]=="OWN"), ["member_id"]]

#Initialize three numpy arrays of loan_amounts that correspond to each member_ids in each of the three series of member_ids
#By providing a member_id, df.loc[] method looks for the value in the same row in the specified column: 'loan_amnt'
#Using a for loop, we could provide all member_ids in the series to retrieve the corresponding loan_amnt value
#We append loan_amnt values into the numpy arrays
MORTGAGE_total = []
for i in MORTGAGE_OWNERS["member_id"]:
    MORTGAGE_total.append(loan_data.loc[loan_data.member_id == i, 'loan_amnt'].values[0])
RENT_total = []
for i in RENT_OWNERS["member_id"]:
    RENT_total.append(loan_data.loc[loan_data.member_id == i, 'loan_amnt'].values[0])
OWN_total = []
for i in OWN_OWNERS["member_id"]:
    OWN_total.append(loan_data.loc[loan_data.member_id == i, 'loan_amnt'].values[0])

#Use the np.mean(int) method to retrieve the average loan amount
#Create a dataframe that contains two series: home ownership type data and average loan amount data
results = pd.DataFrame({'home_ownership':["MORTGAGE","RENT","OWN"], 'loan_amount':[np.mean(MORTGAGE_total),np.mean(RENT_total),np.mean(OWN_total)]})
print(results)
#Using df.plot method to plot a bar graph, with the x axis being home ownership type and the y axis being the average loan amount
plt.table(cellText = results.values, colWidths = [0.25]*len(results.columns), rowLabels=results.index, colLabels = results.columns, cellLoc = 'center', rowLoc = 'center', loc = 'bottom')
fig = plt.gcf()

graph = results.plot.bar(x='home_ownership', y='loan_amount', rot=0, title="Average loan amounts per home ownership")
graph.set_xlabel("Home Ownership Type", fontsize=12)
graph.set_ylabel("Average Loan Amount ($)", fontsize=12)

plt.show()





    