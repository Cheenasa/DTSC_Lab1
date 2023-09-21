#Problem 1

import re
from collections import defaultdict

WORD_RE = re.compile(r"[\w']+")

def tokenize(text):
    return WORD_RE.findall(text)

def map_reduce(filename):
    word_counts = defaultdict(int)

    with open(filename, 'r') as file:
        for line in file:
            words = tokenize(line)
            for word in words:
                word_counts[word.lower()] += 1

    return word_counts

if __name__ == "__main__":
    filename = "/Users/cheerycheena/Downloads/dtsc701_lab2_prb1.txt"  
    word_counts = map_reduce(filename)

    # Print the unique words and their counts
    for word, count in word_counts.items():
        print(f"{word}: {count}")
