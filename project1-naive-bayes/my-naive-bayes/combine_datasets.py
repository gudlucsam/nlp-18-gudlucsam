
# coding: utf-8

# In[1]:


def createDataset(file, dataset):
    """
        writes data from a file to a new file.
    """
    with open(file, 'r') as file1, open(dataset, 'a') as file2:
        for line in file1:
            file2.write(line)
            
        
    


# In[4]:


#createDataset('../sentiment-labelled-sentences/imdb_labelled.txt', '../sentiment-labelled-sentences/mainDataset.txt')
#createDataset('../sentiment-labelled-sentences/amazon_cells_labelled.txt', '../sentiment-labelled-sentences/mainDataset.txt')
#createDataset('../sentiment-labelled-sentences/yelp_labelled.txt', '../sentiment-labelled-sentences/mainDataset.txt')

