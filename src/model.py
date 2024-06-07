from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report
from split import split_data
import numpy as np
import pandas as pd

def model():
    TRAINING_FEATURES, TEST_FEATURES, TRAINING_LABELS, TEST_LABELS = split_data()

    classifier = LogisticRegression(multi_class='multinomial')
    classifier.fit(TRAINING_FEATURES, TRAINING_LABELS)

    PREDICTED_LABELS = classifier.predict(TEST_FEATURES)

    print(classification_report(TEST_LABELS, PREDICTED_LABELS))

model()