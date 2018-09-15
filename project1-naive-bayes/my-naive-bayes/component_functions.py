import csv
import math
from utility_functions import *



def priorProb(csvdatafile, cls):
    """
        This function calculates the probability 
        of a given class in the dataset (the prior probability).
    """
    lst = createList(csvdatafile)
    
    return math.log10(totalCls(lst, cls)/len(lst))

def countWrdsOfVocInCls(csvdatafile, cls):
    """
        Finds the total occurrence of everyword in the vocabulary for a given class.
        It normalizes each word occurrence by adding one to it.
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
    
    countOfWrd = createDict(csvdataset, cls)[wrd.lower] + 1
    
    
    return math.log10(countOfWrd/countWrdsOfVocInCls(csvdataset, cls))



