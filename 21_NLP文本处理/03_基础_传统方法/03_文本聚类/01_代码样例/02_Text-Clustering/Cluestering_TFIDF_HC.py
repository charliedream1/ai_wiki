#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on Wed Feb 27 17:34:06 2019

@author: Preeti
"""

# importing libraries 
import nltk 
import re
from urllib import request
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
stemmer = PorterStemmer()
stop_words = set(stopwords.words('english'))
from nltk.stem import WordNetLemmatizer 
lemmatizer = WordNetLemmatizer() 
from sklearn import metrics
import numpy as np



#Data preparation and preprocess
def custom_preprocessor(text):
        text = re.sub(r'\W+|\d+|_', ' ', text)    #removing numbers and punctuations
        text =  re.sub(r'\s+',' ',text) #remove multiple spaces into a single space
        text = re.sub(r"\s+[a-zA-Z]\s+",' ',text) #remove a single character
        text = text.lower() 
        text = nltk.word_tokenize(text)       #tokenizing
        text = [word for word in text if not word in stop_words] #English Stopwords
        text = [lemmatizer.lemmatize(word) for word in text]              #Lemmatising
        return text
    
    
    
filepath_dict = {'Book1':   'https://www.gutenberg.org/files/58764/58764-0.txt',
               'Book2': 'https://www.gutenberg.org/files/58751/58751-0.txt',
               'Book3':   'http://www.gutenberg.org/cache/epub/345/pg345.txt'}


for key, value in filepath_dict.items():
   if (key == "Book1"):
        bookLoc = filepath_dict[key]
        response = request.urlopen(bookLoc)
        raw = response.read().decode('utf-8')
        len(raw)
        first_book = custom_preprocessor(raw)           
   elif (key == "Book2"):
        bookLoc = filepath_dict[key]
        response = request.urlopen(bookLoc)
        raw = response.read().decode('utf-8')
        len(raw)
        second_book = custom_preprocessor(raw)
   elif (key == "Book3"):
        bookLoc = filepath_dict[key]
        response = request.urlopen(bookLoc)
        raw = response.read().decode('utf-8')
        len(raw)
        third_book = custom_preprocessor(raw)
   else:
       pass
        
        
#Building First Book
first_book_text = ' '.join(first_book)
fileLoc = '/Users/sfuhaid/Desktop/EBC7100Assign2-Group7/firstbook/a.txt'
with open(fileLoc, 'a') as fout:
    fout.write(first_book_text)
    fout.close()

#Building Second Book
second_book_text = ' '.join(second_book)
fileLoc = '/Users/sfuhaid/Desktop/EBC7100Assign2-Group7/secondbook/b.txt'
with open(fileLoc, 'a') as fout:
    fout.write(second_book_text)
    fout.close()
    
 
#Building Third Book
third_book_text = ' '.join(third_book)
fileLoc = '/Users/sfuhaid/Desktop/EBC7100Assign2-Group7/thirdbook/c.txt'
with open(fileLoc, 'a') as fout:
    fout.write(third_book_text)
    fout.close()
    

# labeling
# Cretaing tuple
# aBooklist = []
def readAtxtfile(bookText, docs, labels):
    x = 0
    i = 0
    n = 150
    while x < 200:
        temp = ""
        words = bookText.split(" ")[i:n]
        for word in words:
            temp = word + " " + temp
        docs.append(temp)
        labels.append(0)
        i += 150
        n += 150
        x += 1
    return docs, labels


# Cretaing tuple
# bBooklist = []
def readBtxtfile(bookText, docs, labels):
    x = 0
    i = 0
    n = 150
    while x < 184:
        temp = ""
        words = bookText.split(" ")[i:n]
        for word in words:
            temp = word + " " + temp
        docs.append(temp)
        labels.append(1)
        i += 150
        n += 150
        x += 1
    return docs, labels

# Cretaing tuple
# cBooklist = []
def readCtxtfile(bookText, docs, labels):
    x = 0
    i = 0
    n = 150
    while x < 200:
        temp = ""
        words = bookText.split(" ")[i:n]
        for word in words:
            temp = word + " " + temp
        docs.append(temp)
        labels.append(2)
        i += 150
        n += 150
        x += 1
    return docs, labels


docs = []
labels = []
docs, labels = readAtxtfile(first_book_text, docs, labels)
# print(aBooklist)
docs, labels = readBtxtfile(second_book_text, docs, labels)
# print(bBooklist)
docs, labels = readCtxtfile(third_book_text, docs, labels)
# print(cBooklist)


#print(len(docs))
#print(docs)
#print(labels)
#print(len(labels))

#***********************collocation********************************************
import nltk
from nltk.collocations import *
bigram_measures = nltk.collocations.BigramAssocMeasures()
trigram_measures = nltk.collocations.TrigramAssocMeasures()
# change this to read in your data
finder = BigramCollocationFinder.from_words(first_book+second_book+third_book)
# only bigrams that appear 3+ times
finder.apply_freq_filter(3) 
# return the 10 n-grams with the highest PMI
book_collocation = finder.nbest(bigram_measures.pmi, 10)
#print('collocation : ',book_collocation)


#Tf-IDF Model Implementation
# Creating the Tf-Idf model 

from sklearn.feature_extraction.text import TfidfVectorizer
vectorizer = TfidfVectorizer(max_features = 2000 , min_df = 3, max_df = 0.6)
X = vectorizer.fit_transform(docs)
X.toarray()
#**********************Hierarchical clustering*********************************
def tfidf_hc(X,k):
    from sklearn.cluster import AgglomerativeClustering
    HC_X = X.toarray()
    cluster = AgglomerativeClustering(n_clusters=3, affinity='cosine', linkage='complete', compute_full_tree = 'bool')
    labelsPred = cluster.fit_predict(HC_X)
    return labelsPred
#*****************************calculation**************************************
cluster = tfidf_hc(X, 3)#cluster = 3
#print(cluster)
#kappa algo for evaluation
print (metrics.cohen_kappa_score(labels, cluster,weights = 'linear'))

from scipy.stats import spearmanr
from time import time
name = 'Hierarchical'
t0 = time()

print(82 * '_')
print('init\t\ttime\thomo\tcompl\tv-meas\tARI\tAMI\tkappa\tcorr\tsilh_Clus\tsilh_HMN')
print('%-9s\t%.2fs\t%i\t%.3f\t%.3f\t%.3f\t%.3f\t%.3f\t%-9s\t%.3f\t%.3f'
          % (name, (time() - t0),
             metrics.homogeneity_score(labels, cluster),
             metrics.completeness_score(labels, cluster),
             metrics.v_measure_score(labels, cluster),
             metrics.adjusted_rand_score(labels, cluster),
             metrics.adjusted_mutual_info_score(labels,  cluster),
             metrics.cohen_kappa_score(labels, cluster,weights = 'linear'),
             str(spearmanr(labels,cluster)),
             metrics.silhouette_score(X, cluster),
             metrics.silhouette_score(X, labels),
             ))

#**************************error analysis**************************************
from sklearn.metrics.cluster import contingency_matrix
x = labels #actual labels
y = cluster #predicted labels
error_analysis = contingency_matrix(x, y)
#***************************plot************************************************
#visulization
from scipy.cluster import hierarchy
import matplotlib.pyplot as plt
X = np.array(X.toarray())
X = X[:20]
Z = hierarchy.linkage(X, 'complete')
plt.figure()
dn = hierarchy.dendrogram(Z)
plt.show()

