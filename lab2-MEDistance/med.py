from argparse import ArgumentParser
import numpy as np



def sub_cost(cha_i, cha_j):
    """checks if two characters are equal"""

    if cha_i == cha_j:
        return 0
    else:
        return 2

def meDistance(source_word, target_word):
    """calculates the minimum edit distance between two words"""
    # normalize wordds
    source_word = source_word.lower()
    target_word = target_word.lower()

    n = len(source_word)
    m = len(target_word)

    # initialize numpy
    arr = np.zeros((n+1, m+1))
    
    arr[0, 0] = 0
    for i in range(1, n+1):
        arr[i, 0] = arr[i-1, 0]+1
    for j in range(1, m+1):
        arr[0, j] = arr[0, j-1]+1

    # recurrence
    for i in range(1, n+1):
        for j in range(1, m+1):
            arr[i, j] = min(arr[i-1, j]+1, arr[i-1, j-1]+sub_cost(source_word[i-1], target_word[j-1]), arr[i, j-1]+1)

    return arr[n, m]


if __name__ == '__main__':
    # accept command-line arguments
    parser = ArgumentParser(description="calculates the minimum edit distance between two words.")
    parser.add_argument("source_word", help="takes the source word")
    parser.add_argument("target_word", help="takes the target word")
    args = vars(parser.parse_args())

    # extract arguments passed from command-line
    source_word = args.get('source_word', None)
    target_word = args.get('target_word', None)

    if source_word and target_word:
        md = meDistance(source_word, target_word)
        print("the minimum edit distance between {0} and {1} is {2}".format(source_word, target_word, str(md)))
    
