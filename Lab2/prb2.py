import re
#import string

stop_words = ["the", "and", "of", "a", "to", "in", "is", "it"]

def map_non_stop_words(line):
    words = re.sub(r'\W', ' ', line.lower().strip())
    words = words.split()
    non_stop_words = [word for word in words if word not in stop_words]
    word_count = []
    for word in non_stop_words:
        word_count.append((word, 1))
    return word_count

l = "This is a sample input text. It contains some common words such as the, and, of, a, and to. These stopwords should be removed in the output"
map_non_stop_words(l)
