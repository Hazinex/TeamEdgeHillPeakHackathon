import pandas as pd
from sklearn.model_selection import train_test_split
from cleaning import clean

def split_data():
    dataset = clean()

    # Splits into chunks to ensure balanced training and test data
    chunk_1 = dataset.loc[(dataset["Quantity"] >= 1) & (dataset["Quantity"] <= 5)] #1-5
    chunk_2 = dataset.loc[(dataset["Quantity"] >= 6) & (dataset["Quantity"] <= 10)] #6-10
    chunk_3 = dataset.loc[(dataset["Quantity"] >= 11) & (dataset["Quantity"] <= 14)] #6-10

    # Finds 80% for training and 20% for test
    X1_train, X1_test, Y1_train, Y1_test = train_test_split(chunk_1.drop(columns=['Quantity']), chunk_1['Quantity'], test_size=0.2)
    X2_train, X2_test, Y2_train, Y2_test = train_test_split(chunk_2.drop(columns=['Quantity']), chunk_2['Quantity'], test_size=0.2)
    X3_train, X3_test, Y3_train, Y3_test = train_test_split(chunk_3.drop(columns=['Quantity']), chunk_3['Quantity'], test_size=0.2)

    # Concatenates the dataframes
    TRAINING_FEATURES = pd.concat([X1_train, X2_train, X3_train])
    TEST_FEATURES = pd.concat([X1_test, X2_test, X3_test])
    TRAINING_LABELS = pd.concat([Y1_train, Y2_train, Y3_train])
    TEST_LABELS = pd.concat([Y1_test, Y2_test, Y3_test])

    return TRAINING_FEATURES, TEST_FEATURES, TRAINING_LABELS, TEST_LABELS