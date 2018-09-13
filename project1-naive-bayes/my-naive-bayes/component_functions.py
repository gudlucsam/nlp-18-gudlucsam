

import csv
import math
from utility_functions import *





def priorProb(csvdatafile, cls):
    """
    this function calculates the probability 
    of a given class in the dataset (Prior Probability).
    """
    lst = createList(csvdatafile)
    
    return math.log10(totalCls(lst, cls)/len(lst))

def countWrdsOfVocInCls(csvdatafile, cls):
    """
        Finds the sum of the occurrence of everyword in the vocabulary in a given class.
        it normalizes each word occurrence by adding one to it.
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



