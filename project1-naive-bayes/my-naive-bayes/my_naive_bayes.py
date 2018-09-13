
# coding: utf-8

# In[ ]:


import csv
import math
from collections import Counter

def createList(csvdatafile):
    """
        creates a python list with data in csv.
    """
    with open(csvdatafile, 'r') as f:
        reader = csv.reader(f)
        lst = list(reader)
        
        return lst

def totalCls(lst, cls):
    """
        returns the total counts of a particular class.
    """
    count = 0
    for i in lst:
        if i and i[-1] == cls:
                count+=1
                
    return count
            
    
def priorProb(csvdatafile, cls):
    """
    this function calculates the probability 
    of a given class given the dataset.
    """
    lst = createList(csvdatafile)
    
    return math.log10(totalCls(lst, cls)/len(lst))

def createDict(csvdatafile, cls):
    """
        create a dictionary of word count given a class.
    """
    cnt = Counter()
    lst = createList(csvdatafile)
    d = {}
    for i in lst:
        if i and int(i[-1]) == cls:
            cnt.update(map(str.lower, i[:-1]))
    return cnt

def countWrdsOfVocInCls(csvdatafile, cls):
    """
        Finds the sum of the occurrence of everyword in the vocabulary given a class.
        it normalizes the each word occurrence by adding one to it.
    """
    
    datasetCounts = createDict(csvdatafile, 1) + createDict(csvdatafile, 0)
    
    if int(cls) == 1:
        counts = createDict(csvdatafile, 1)
    else:
        counts = createDict(csvdatafile, 0)
    
    cnt = 0
    for wrd in datasetCounts:
        cnt+=counts[wrd] + 1
    
    return cnt
        
    
def likelihoodOfWordInCls(wrd, cls):
    """
        Finds the probability of a word in a class.
    """
    csvdataset = '../sentiment-labelled-sentences/mainDataset.csv'
    
    countOfWrd = createDict(csvdataset, cls)[wrd] + 1
    
    
    return math.log10(countOfWrd/countWrdsOfVocInCls(csvdataset, cls))


#def classifier(testdoc, logprior, loglikelihood, C, V):
    
    
    
    
    
    

