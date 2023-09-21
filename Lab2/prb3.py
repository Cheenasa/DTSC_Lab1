#importing relevant libraries
import string #to manipulate string variables and remove punctuation marks.

# Define the documents to be inverted
document1 = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit.'
document2 = 'Donec condimentum elit vel mauris varius, id laoreet tortor placerat.'
document3 = 'Nulla scelerisque felis ac risus varius, sit amet luctus elit mattis.'

#Remove punctuation marks from the documents
for punctuation in string.punctuation:
    document1 = document1.replace(punctuation, '')
    document2 = document2.replace(punctuation, '')
    document3 = document3.replace(punctuation, '')

#Tokenize the documents
# Convert each document to lowercase and split it into words
tokens1 = document1.lower().split()
tokens2 = document2.lower().split()
tokens3 = document3.lower().split()
 
# Combine the tokens into a list of unique terms
words = list(set(tokens1 + tokens2 + tokens3))
 
# Step 2: Build the inverted index
# Create an empty dictionary to store the inverted index
inverted_index = {}
 
# For each term, find the documents that contain it
for word in words:
    documents = []
    if word in tokens1:
        documents.append("Document 1")
    if word in tokens2:
        documents.append("Document 2")
    if word in tokens3:
        documents.append("Document 3")
    inverted_index[word] = documents
 
# Step 3: Print the inverted index
for word, documents in inverted_index.items():
    print(word, "->", ", ".join(documents))
