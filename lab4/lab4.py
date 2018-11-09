import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer

from sklearn.naive_bayes import MultinomialNB
from sklearn.linear_model import LogisticRegression

from sklearn.metrics import classification_report
# print(classification_report(y_test, y_pred))






# read dataset with pandas
data = pd.read_csv('dataset.txt', delimiter="\t", names=['sentences', 'labels'])
# split data into training and testing data
X_train, X_test, y_train, y_test = train_test_split(data['sentences'], data['labels'], test_size=0.3)

# =============Naive Bayes Un-normalized============ # 

def uNaiveBayesTrain():
    """ Training an unnormalized naivebayes model """

    # initialize CountVectorizer to extract word features
    count_vect = CountVectorizer()

    # transform training dataset to word features without normalizing
    X_train_features = count_vect.fit_transform(X_train)
    
    # train model with training dataset
    clf = MultinomialNB().fit(X_train_features, y_train)

    # return trained model
    return clf, count_vect


def uPredict(test_file, resultdoc="result-nb-u.txt"):
    """ predicting when given a test file"""

    # call trained model
    clf, count_vect  = uNaiveBayesTrain()

    # load test data
    data = []
    with open(test_file, 'r') as f:
        for sentence in f:
            data.append(sentence.strip('\r\n'))

    # transform test_data to features
    X_test_features = count_vect.transform(data) 

    # predict test sentences
    predicted = clf.predict(X_test_features)
    
    # write prediction to file
    with open(resultdoc, 'w', newline='') as f1:
        for prediction in predicted:
            f1.write(str(prediction) + '\n')

def uAccuracy():
    """ calculates the accuracy of the unnormalized naive bayes model"""
    # call trained model
    clf, count_vect  = uNaiveBayesTrain()

    # transform test_data to features
    X_test_features = count_vect.transform(X_test)

    # make prediction
    predicted = clf.predict(X_test_features)

    # calculate accuracy
    acc = np.mean(predicted == y_test)
    # print accuracy
    print("Accuracy of un-normalized naive bayes is: " + str(round(acc, 3)))




# =============Naive Bayes normalized============ # 

def nNaiveBayesTrain():
    """ Training normalized naivebayes model """

    # initialize CountVectorizer to extract word features with normalization
    count_vect = CountVectorizer(stop_words="english", analyzer='word', 
                            ngram_range=(1, 1), max_df=0.5, min_df=1, max_features=None)

    # transform training dataset to word features 
    X_train_features = count_vect.fit_transform(X_train)

    # solve frequency discrepancies among long and short sentences
    tfidf_transformer = TfidfTransformer()
    X_train_tfidf = tfidf_transformer.fit_transform(X_train_features)
    
    # train model with training dataset
    clf = MultinomialNB().fit(X_train_tfidf, y_train)

    # return trained model
    return clf, count_vect, tfidf_transformer


def nPredict(test_file, resultdoc="result-nb-n.txt"):
    """ predicting when given a test file"""

    # call trained model
    clf, count_vect, tfidf_transformer  = nNaiveBayesTrain()

    # load test data
    data = []
    with open(test_file, 'r') as f:
        for sentence in f:
            data.append(sentence.strip('\r\n'))

    # transform test_data to features
    X_test_features = count_vect.transform(data) 
    # solve frequency discrepancies among short and long sentences
    X_new_tfidf = tfidf_transformer.transform(X_test_features)

    # predict test sentences
    predicted = clf.predict(X_new_tfidf)
    
    # write prediction to file
    with open(resultdoc, 'w', newline='') as f1:
        for prediction in predicted:
            f1.write(str(prediction) + '\n')


def nAccuracy():
    """ calculates the accuracy of the normalized naive bayes model"""
    
    # call trained model
    clf, count_vect, tfidf_transformer  = nNaiveBayesTrain()

    # transform test_data to features
    X_test_features = count_vect.transform(X_test)

    # make prediction
    predicted = clf.predict(X_test_features)

    # calculate accuracy
    acc = np.mean(predicted == y_test)
    # print accuracy
    print("Accuracy of normalized naive bayes is: " + str(round(acc, 3)))






# =============Logistic Regression un-normalized============ # 

def uLogisticRegressionTrain():
    """ Training an unnormalized logistic regression model """

    # initialize CountVectorizer to extract word features without normalization
    count_vect = CountVectorizer()

    # transform training dataset to word features without normalizing
    X_train_features = count_vect.fit_transform(X_train)
    
    # train model with training dataset
    logreg = LogisticRegression(solver='lbfgs').fit(X_train_features, y_train)

    # return trained model
    return logreg, count_vect


def ulrPredict(test_file, resultdoc="result-lr-u.txt"):
    """ predicting when given a test file"""

    # call trained model
    logreg, count_vect  = uLogisticRegressionTrain()

    # load test data
    data = []
    with open(test_file, 'r') as f:
        for sentence in f:
            data.append(sentence.strip('\r\n'))

    # transform test_data to features
    X_test_features = count_vect.transform(data) 

    # predict test sentences
    predicted = logreg.predict(X_test_features)
    
    # write prediction to file
    with open(resultdoc, 'w', newline='') as f1:
        for prediction in predicted:
            f1.write(str(prediction) + '\n')

def ulrAccuracy():
    """ calculates the accuracy of the unnormalized logistic regresion model"""
    # call trained model
    logreg, count_vect  = uLogisticRegressionTrain()

    # transform test_data to features
    X_test_features = count_vect.transform(X_test)

    # make prediction
    predicted = logreg.predict(X_test_features)

    # calculate accuracy
    acc = np.mean(predicted == y_test)
    # print accuracy
    print("Accuracy of un-normalized logistic regression model is: " + str(round(acc, 3)))




# =============Logistic Regression normalized============ # 

def nLogisticRegressionTrain():
    """ Training normalized logistic regression model """

    # initialize CountVectorizer to extract word features with normalization
    count_vect = CountVectorizer(stop_words="english", analyzer='word', 
                            ngram_range=(1, 1), max_df=0.5, min_df=1, max_features=None)

    # transform training dataset to word features 
    X_train_features = count_vect.fit_transform(X_train)

    # solve frequency discrepancies among long and short sentences
    tfidf_transformer = TfidfTransformer()
    X_train_tfidf = tfidf_transformer.fit_transform(X_train_features)
    
    # train model with training dataset
    logreg = LogisticRegression(solver='lbfgs').fit(X_train_tfidf, y_train)

    # return trained model
    return logreg, count_vect, tfidf_transformer


def nlrPredict(test_file, resultdoc="result-lr-n.txt"):
    """ predicting when given a test file"""

    # call trained model
    logreg, count_vect, tfidf_transformer  = nLogisticRegressionTrain()

    # load test data
    data = []
    with open(test_file, 'r') as f:
        for sentence in f:
            data.append(sentence.strip('\r\n'))

    # transform test_data to features
    X_test_features = count_vect.transform(data) 
    # solve frequency discrepancies among short and long sentences
    X_new_tfidf = tfidf_transformer.transform(X_test_features)

    # predict test sentences
    predicted = logreg.predict(X_new_tfidf)
    
    # write prediction to file
    with open(resultdoc, 'w', newline='') as f1:
        for prediction in predicted:
            f1.write(str(prediction) + '\n')


def nlrAccuracy():
    """ calculates the accuracy of the normalized logistic regression model"""
    
    # call trained model
    logreg, count_vect, tfidf_transformer = nLogisticRegressionTrain()

    # transform test_data to features
    X_test_features = count_vect.transform(X_test)

    # make prediction
    predicted = logreg.predict(X_test_features)

    # calculate accuracy
    acc = np.mean(predicted == y_test)
    # print accuracy
    print("Accuracy of normalized logistic regression is: " + str(round(acc, 3)))




if __name__ == '__main__':
    # un-normalized  naive bayes
    # uPredict('imdb_labelled.txt')
    # uAccuracy()

    # normalized naive bayes
    # nPredict('imdb_labelled.txt')
    # nAccuracy()


    # un-normalized logistic regression
    ulrPredict('imdb_labelled.txt')
    ulrAccuracy()


    # normalized logistic regression
    nlrPredict('imdb_labelled.txt')
    nlrAccuracy()