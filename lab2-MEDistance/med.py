import numpy as np


def sub_cost(cha_i, cha_j):
    """ checks if two characters are equal"""

    if cha_i == cha_j:
        return 0
    else:
        return 2

def meDistance(source_word, target_word):
    """calculates the minimum edit distance between two words"""
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
    md = meDistance("intention", "execution")
    print("the minimum edit distance between {0} and {1} is {2}".format("dog", "cat", str(md)))
    
