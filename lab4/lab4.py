import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split

import nltk
from nltk.corpus import stopwords
from nltk.classify import SklearnClassifier



# =========== READ DATA ==================
data = pd.read_csv('dataset.txt', delimiter="\t")

# split data into training and testing data
train, test = train_test_split(data, test_size=0.3)

stop_words_set = set(stopwords.words("english"))
print(stop_words_set)