import csv
import math
from collections import Counter



class model:
    """ A model for naive base classifier"""
    def __init__(self, v, c):
        self.vocabulary = v
        self.cls = c
        self.log_prior = {}
        self.word_counts = {}
        self.total_reviews_in_cls = {}
        self.freq_of_words_in_cls = {}
        self.log_likelihood_of_word = {}

    def create_list(self):
        """
            creates a python list from data in csv format.
        """
        with open(self.vocabulary, 'r') as f:
            reader = csv.reader(f)
            lst = list(reader)

        self.lst = lst

    def getList(self):
        """
            list getter
        """
        return self.lst

    def create_dict_of_words_count(self):
        """
            creates a dictionary of words count for words in a class.
        """
        for clss in self.cls:
            cnt = Counter()
            for i in self.lst:
                if i and int(i[-1]) == clss:
                    cnt.update([item.lower() for item in i[:-1]])

            self.word_counts[clss] = cnt

    def getDictOfWordCounts(self):
        """
            a getter function for word_counts
        """
        return self.word_counts

    def total_counts_of_reviews_in_cls(self):
        """
            returns the total counts of reviews for each class.
        """
        for clss in self.cls:
            count = 0
            for i in self.lst:
                if i and int(i[-1]) == clss:
                    count+=1
            self.total_reviews_in_cls[clss] = count
        
    def getTotalCountsOfReviews(self):
        """
            getter function for total_counts_of_reviews_in_cls
        """
        return self.total_reviews_in_cls

    def overall_reviews_in_dataset(self):
        """
            returns the total reviews in the dataset.
        """
        self.totalCounts = len(self.lst)

    def getOverallCountOfReviews(self):
        """
            getter function for counts of overall reviews in dataset.
        """
        return self.totalCounts
        
    def find_prior(self):
        """
            this function calculates the prior probability 
            for each class in the dataset.
        """
        for clss in self.cls:
            self.log_prior[clss] = math.log(self.total_reviews_in_cls[clss]/self.totalCounts)

    def getLogPrior(self):
        """
            returns log_prior for every class.
        """
        return self.log_prior

    def distinct_words_in_v(self):
        """
            returns a dictionary of all words and their counts in the v.
        """
        distinct_words = Counter()
        for key in self.word_counts:
            distinct_words+=self.word_counts[key]

        self.distinct_words = distinct_words
    
    def getDistinctWords(self):
        """
            returns distinct words in v in a Counter.
        """
        return self.distinct_words

    def words_occurence_in_cls(self):
        """
            Finds the total occurrence of every word in the vocabulary in a class.
            It normalizes each word occurrence by adding one to it.
        """
        for clss in self.cls:
            word_counts_for_cls = self.word_counts[clss]

            cnt = 0
            for word in self.distinct_words:
                cnt +=word_counts_for_cls[word] + 1
            
            self.freq_of_words_in_cls[clss] = cnt
    
    def getFreqOfWordsInCls(self):
        """
            getter function for frequency of every word in v in each class.
        """
        return self.freq_of_words_in_cls

    def log_likelihood_of_word_in_cls(self, word):
        """
            finds the probability of a word in a class.
        """
        word = word.lower()
        values = {}
        for clss in self.cls:
            count_of_word = self.word_counts[clss][word] + 1
            likelihood = math.log(count_of_word/self.freq_of_words_in_cls[clss])
            values[clss] = likelihood
            
            self.log_likelihood_of_word[word] = values

    def getLogLikihoodOfWordInCls(self):
        """
            returns the log_likihood of a word in each class.
        """
        return self.log_likelihood_of_word

    def train(self):
        """
            this function trains the model with a dataset.
        """
        self.create_list()
        #print(self.getList())
        self.create_dict_of_words_count()
        #print(self.getDictOfWordCounts()[1])
        self.total_counts_of_reviews_in_cls()
        #print(self.getTotalCountsOfReviews()[0])
        self.overall_reviews_in_dataset()
        #print(self.getOverallCountOfReviews())
        self.find_prior()
        #print(self.getLogPrior()[0])
        self.distinct_words_in_v()
        #print(self.getDistinctWords())
        self.words_occurence_in_cls()
        #print(self.getFreqOfWordsInCls()[0])
        #self.log_likelihood_of_word_in_cls('bad')
        #print(self.getLogLikihoodOfWordInCls()['bad'][0])

    def likelihood_of_review(self, review, clss):
        """
            calculates the likelihood of an entire review in a class.
        """
        # sanitize review
        review = review.strip(' \n\t')
        for ch in [',', ';', '.', '"', '!', '(', ')', ':', '/', "-", '\\', '?' ]:
            if ch in review:
                review = review.replace(ch, ' ')

        lst = list(review.strip().split())
        
        likelihood = 0
        for word in lst:
            word = word.lower()
            self.log_likelihood_of_word_in_cls(word)
            likelihood+=self.getLogLikihoodOfWordInCls().get(word, 0)[clss]

        return likelihood

    def naive_bayes_classifier(self, testdoc, resultsdoc="../sentiment-labelled-sentences/result.txt"):
        """
            this function takes a testdoc.txt file containing a several sentences each sentence representing a review.
            and creates a resultsdoc file (passed to function as argument) containing computed labels for each review.
            it also returns a list of assigned labels to help compute the accuracy of the model
        """
        labels = []
        with open(testdoc, 'r') as f1, open(resultsdoc, 'w',  newline='') as f2:
            for review in f1:
                prob = []
                for clss in self.cls:
                    # returns logprior of class
                    logPrior = self.getLogPrior()[clss]
                    # return likelihood of review
                    likelihoodOfReview = self.likelihood_of_review(review, clss)
                    # return probability of review in a class
                    probOfReview = likelihoodOfReview + logPrior
                    # append probability to list
                    prob.append(probOfReview)
                    
                # select assigned label for review
                label = prob.index(max(prob))
                # appends results to list to help compute the accuracy
                labels.append(label) 
                # write results to file
                f2.write(str(label) + '\n')
                
            self.labels = labels
            
    def compute_accuracy(self, testdoc, newtestdoc="../sentiment-labelled-sentences/newdoc.txt"):
        """
            This function measures the accuracy of the model with labelled dataset.
        """
        # cleaning testdoc data with labels to newtestdoc without labels
        known_labels = []
        with open(newtestdoc, 'w', newline='') as f1, open(testdoc, 'r') as f2:
            for review in f2:
                testReview, cls = review.split("\t")
                known_labels.append(int(cls.strip()))
                f1.write(testReview + "\n")
                
        # naive bayes classifier
        self.naive_bayes_classifier(newtestdoc)
        
        # computing accuracy
        matchCount = 0
        for i in range(len(known_labels)):
            if known_labels[i] == self.labels[i]:
                matchCount+=1
                
        # compute accuracy
        self.accuracy = matchCount/len(known_labels)  

    def getAccuracy(self):
        """
            returns the accuracy of the model.
        """
        return self.accuracy


if __name__ == '__main__':
    # instantiate model
    mdl = model('../sentiment-labelled-sentences/mainDataset.csv', [0,1])
    # train model
    mdl.train()
    # start classifiers
    mdl.naive_bayes_classifier("../sentiment-labelled-sentences/test.txt")
    # measure accuracy with 30% of dataset.
    mdl.compute_accuracy("../sentiment-labelled-sentences/test.txt")
    print(mdl.getAccuracy())
