import pandas as pd
from joblib import load, dump
import os
import datetime
import numpy as np

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

# Code for consumer analysis
consumerDF = dataset[dataset['Segment'] == "Consumer"]
purchasePatterns(consumerDF)