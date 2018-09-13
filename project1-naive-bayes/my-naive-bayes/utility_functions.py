
import csv
import math
from collections import Counter



def createList(csvdatafile):
    """
        creates a python list from data in csv format.
    """
    with open(csvdatafile, 'r') as f:
        reader = csv.reader(f)
        lst = list(reader)
        
        return lst
    

def createDict(csvdatafile, cls):
    """
        create a dictionary of words count given a class in the dataset.
    """
    cnt = Counter()
    lst = createList(csvdatafile)
    for i in lst:
        if i and int(i[-1]) == cls:
            cnt.update(map(str.lower, i[:-1]))
    return cnt
    
    
def totalCls(lst, cls):
    """
        returns the total counts of a class in dataset.
    """
    count = 0
    for i in lst:
        if i and int(i[-1]) == cls:
            count+=1
                
    return count
            

    

    
            

