
# coding: utf-8

# In[48]:


import csv
import math




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
    
            
            
                


# In[49]:


priorProb('../sentiment-labelled-sentences/mainDataset.csv', '1')

