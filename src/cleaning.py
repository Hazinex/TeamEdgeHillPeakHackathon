import os
from joblib import load, dump
import pandas as pd
from sklearn.calibration import LabelEncoder

def clean():
    # Loads the joblib
    if os.path.exists("dataset.joblib"):
        dataset = load("dataset.joblib")
    else:
        dataset = pd.read_excel("Superstore Dataset.xlsx", index_col=0)
        dump(dataset, "dataset.joblib")

    # Encodes all the columns that have textual data, to ensure models can 
    # be executed
    encoder = LabelEncoder()
    dataset['Order ID'] = encoder.fit_transform(dataset['Order ID'])
    dataset['Order Date'] = encoder.fit_transform(dataset['Order Date'])
    dataset['Ship Date'] = encoder.fit_transform(dataset['Ship Date'])
    dataset['Ship Mode'] = encoder.fit_transform(dataset['Ship Mode'])
    dataset['Customer ID'] = encoder.fit_transform(dataset['Customer ID'])
    dataset['Customer Name'] = encoder.fit_transform(dataset['Customer Name'])
    dataset['Segment'] = encoder.fit_transform(dataset['Segment'])
    dataset['Country'] = encoder.fit_transform(dataset['Country'])
    dataset['City'] = encoder.fit_transform(dataset['City'])
    dataset['State'] = encoder.fit_transform(dataset['State'])
    dataset['Region'] = encoder.fit_transform(dataset['Region'])
    dataset['Product ID'] = encoder.fit_transform(dataset['Product ID'])
    dataset['Category'] = encoder.fit_transform(dataset['Category'])
    dataset['Sub-Category'] = encoder.fit_transform(dataset['Sub-Category'])
    dataset['Product Name'] = encoder.fit_transform(dataset['Product Name'])

    return dataset

