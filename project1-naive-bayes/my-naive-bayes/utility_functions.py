import csv



def merge_dataset(file, dataset):
    """
        writes data from a file to another file.
    """
    with open(file, 'r') as file1, open(dataset, 'a') as file2:
        for line in file1:
            file2.write(line)
            
def convert_to_csv(txtfile, csvfile):
    """
        converts a txt file into a csv
    """
    with open(txtfile, 'r') as f1, open(csvfile, 'w', newline='') as f2:
        out_file = csv.writer(f2)
        for line in f1:
            line = line.strip(' \n\t')
            for ch in [',', ';', '.', '"', '!', '(', ')', ':', '/', "-", '\\', '?' ]:
                if ch in line:
                    line = line.replace(ch, ' ')
            out_file.writerow(list(line.strip().split()))

    
