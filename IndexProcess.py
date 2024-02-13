# -------------------------------------------------------------------------
# AUTHOR: Christian Williams
# FILENAME: IndexProcess.py
# SPECIFICATION: This program reads documents and determines weights of index terms
#                by performing stopword removal and stemming and finally performs
#                calculations
# FOR: CS 4250- Assignment #1
# TIME SPENT: 2.5 hours
# -----------------------------------------------------------*/


# Importing some Python libraries
import csv
import math

documents = []

# Reading the data in a csv file
with open('collection.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    for i, row in enumerate(reader):
        if i > 0:  # skipping the header
            documents.append(row[0])

# Conducting stopword removal. Hint: use a set to define your stopwords.

# List for documents without the stopwords
newSentence = []

# List of new documents without stop words
newList2 = []

# Contains all stop words
stopWords = {"I", "and", "She", "her", "They", "their"}

# Removes stop words from each document and adds to a new list
for sentence in documents:
    newDocs = sentence.split()
    for word in newDocs:
        if word in stopWords:
            newDocs.remove(word)
    newSentence = (' '.join(newDocs))
    newList2.append(newSentence)

# Conducting stemming. Hint: use a dictionary to map word variations to their stem.
stemming = {"cats": "cat", "loves": "love", "dogs": "dog"}

# Holds changed words after stemming
stemDocs = []

# Holds changes sentences after stemming
newPhrase = []

# Changes all words to stem
for phrase in newList2:
    splitSentence = phrase.split()
    for word2 in splitSentence:
        if word2 in stemming:
            newWord = stemming[word2]
            newPhrase = phrase.replace(word2, newWord)
    stemDocs.append(newPhrase)

# Identifying the index terms.
terms = []

# Adds all words that are indexed into terms[]
for words in stemDocs:
    splitWords = words.split()
    for term in splitWords:
        if term not in terms:
            terms.append(term)

# Building the document-term matrix by using the tf-idf weights.
docTermMatrix = {}

# Gets the number of index terms
length = len(terms)
document_lengths = []
for i in range(length):
    document_lengths.append(i + 1)


# new function to calculate how many documents a specific word shows up in
def idf_count(tfterm):
    count = 0
    for docs2 in stemDocs:
        new = docs2.split()
        if new.count(tfterm) > 0:
            count = count + 1

    return count


# for index purposes
j = 0

# Calculates the tf-idf of each word in each document
for docs in stemDocs:
    docTermMatrix[j] = []
    for index in terms:
        findTerms = docs.split()
        number = docs.count(index)

        # calculates tf
        tf = number / len(findTerms)

        #calculates idf
        idf = math.log((len(stemDocs) / idf_count(index)), 10)

        #calculates tf-idf
        tf_idf = idf * tf
        docTermMatrix[j].append(round(tf_idf, 2))
    j = j + 1

# Printing the document-term matrix

# Prints header first
print("            ", *terms)

#prints matrix values
for i in range(len(document_lengths)):
    print("document", document_lengths[i], ":", *docTermMatrix[i])
