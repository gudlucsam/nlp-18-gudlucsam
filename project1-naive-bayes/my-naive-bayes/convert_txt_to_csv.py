
import csv


def convertToCSV(txtfile, csvfile):
    """
        converts a txt file into a csv
    """
    
    with open(txtfile, 'r') as f1, open(csvfile, 'w') as f2:
        for line in f1:
            for ch in [',', ';', '.', '"', '!', '(', ')', ':', '/', "-", '\\' ]:
                if ch in line:
                    line = line.replace(ch, ' ')
            out_file = csv.writer(f2)
            out_file.writerow(list(line.split()))
    


#convertToCSV('../sentiment-labelled-sentences/mainDataset.txt', '../sentiment-labelled-sentences/mainDataset.csv')

