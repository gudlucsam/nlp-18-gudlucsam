

def combineDataset(file, dataset):
    """
        writes data from a file to a new file.
    """
    with open(file, 'r') as file1, open(dataset, 'a') as file2:
        for line in file1:
            file2.write(line)
            
        