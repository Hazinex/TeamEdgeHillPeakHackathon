import pandas as pd
from joblib import load, dump
import os
import datetime
import numpy as np
import matplotlib.pyplot as plt

# Loads the joblib, this simply speeds up execution as loading from the excel file took ~10 seconds each execution
if os.path.exists("dataset.joblib"):
    dataset = load("dataset.joblib")
else:
    dataset = pd.read_excel("Superstore Dataset.xlsx", index_col=0)
    dump(dataset, "dataset.joblib")

dataset.sort_values(by=['Order Date'], inplace=True)

# Function to analyse the frequency of orders from a customer segment. not working
def purchasePatterns(df):
    dateList = []
    for idx, row in df.iterrows():
        dateList.append(row[1].to_pydatetime())

    print(dateList)

    dateDiffs = []
    for i in range(len(dateList) - 1):
        dateDiffs.append((dateList[i+1] - dateList[i]).days)
    print(dateDiffs)

    print("average distance is: ", np.mean(dateDiffs))

def orderSize(df, segmentStr):
    overall = np.mean(df['Quantity'])
    office = np.mean(df[df['Category'] == 'Office Supplies']['Quantity'])
    furniture = np.mean(df[df['Category'] == 'Furniture']['Quantity'])
    tech = np.mean(df[df['Category'] == 'Technology']['Quantity'])
    print(f"The overall average order quantity for the {segmentStr} segment was: {overall}") # Overall quanitity
    print(f"The average order quantity for the {segmentStr} segment in Office Supplies was {office}") # Office Supplies
    print(f"The average order quantity for the {segmentStr} segment in Furniture was {furniture}") # Office Supplies
    print(f"The average order quantity for the {segmentStr} segment in Technology was {tech}") # Office Supplies
    return [overall, office, furniture, tech]

# Code for consumer analysis
consumerDF = dataset[dataset['Segment'] == "Consumer"]
# purchasePatterns(consumerDF)
consumerVals = orderSize(consumerDF, "Consumer")

# Code for home office
homeOfficeDF = dataset[dataset['Segment'] == "Home Office"]
# purchasePatterns(homeOfficeDF)
homeOfficeVals = orderSize(homeOfficeDF, "Home Office")

# Code for Corporate
corporateDF = dataset[dataset['Segment'] == "Corporate"]
# purchasePatterns(corporateDF)
corporateVals = orderSize(corporateDF, "Corporate")

ex = ['Overall','Office','Furniture','Technology'] 
x_axis = np.arange(len(ex))
print()

fig, ax = plt.subplots()
ax.bar(x_axis - 0.2, consumerVals, 0.2, label="Consumer")
ax.bar(x_axis, homeOfficeVals, 0.2, label="Home Office")
ax.bar(x_axis + 0.2, corporateVals, 0.2, label="Corporate")
ax.set(ylim=[3.6, 3.9])
ax.set_title("Graph of Order Quantities by Segment and Product Category")
ax.set_xticks(x_axis, ex)
ax.set_ylabel("Order Size")

plt.show()