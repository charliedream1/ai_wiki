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
vectorizer = TfidfVectorizer(max_features = 2000, min_df = 3, max_df = 0.6)
TF_X = vectorizer.fit_transform(docs)
TF_X.toarray()


#**********************Expectation Maximization********************************
def tfidf_EM(TF_X):
    from sklearn.mixture import GaussianMixture
    X_EM = TF_X.toarray()
    gmm = GaussianMixture(n_components=3, random_state=0)
    gmm = gmm.fit(X_EM)
    EM_labels = gmm.predict(X_EM)
    return EM_labels

#*****************************calculation**************************************
from scipy.stats import spearmanr
from time import time
from sklearn import metrics

name = 'EM-tfidf'
t0 = time()
EM_label = tfidf_EM(TF_X)
print(82 * '_')
print('init\t\ttime\thomo\tcompl\tv-meas\tARI\tAMI\tkappa\tcorr\tsilh_Clus\tsilh_HMN')
print('%-9s\t%.2fs\t%i\t%.3f\t%.3f\t%.3f\t%.3f\t%.3f\t%-9s\t%.3f\t%.3f'
          % (name, (time() - t0), 
             metrics.homogeneity_score(labels, EM_label),
             metrics.completeness_score(labels, EM_label),
             metrics.v_measure_score(labels, EM_label),
             metrics.adjusted_rand_score(labels, EM_label),
             metrics.adjusted_mutual_info_score(labels,  EM_label),
             metrics.cohen_kappa_score(labels, EM_label,weights='linear'),
             str(spearmanr(labels,EM_label)),
             metrics.silhouette_score(TF_X, EM_label,
                                      metric='euclidean'),
             metrics.silhouette_score(TF_X, labels,
                                      metric='euclidean'),
             ))

#**************************error analysis**************************************
from sklearn.metrics.cluster import contingency_matrix
x = labels #actual labels
y = EM_label #predicted labels
error_analysis = contingency_matrix(x, y)
#***************************plot************************************************
from sklearn.metrics.pairwise import cosine_similarity
dist = 1 - cosine_similarity(TF_X)


import matplotlib.pyplot as plt
import pandas as pd
from sklearn.manifold import MDS
MDS()
# convert two components as we're plotting points in a two-dimensional plane
# "precomputed" because we provide a distance matrix
# we will also specify `random_state` so the plot is reproducible.
mds = MDS(n_components=2, dissimilarity="precomputed", random_state=1)
pos = mds.fit_transform(dist)  # shape (n_components, n_samples)
xs, ys = pos[:, 0], pos[:, 1]


#set up colors per clusters using a dict
cluster_colors = {0: '#1b9e77', 1: '#d95f02', 2: '#7570b3'}

#set up cluster names using a dict
cluster_names = {0: 'first book', 
                 1: 'second book', 
                 2: 'third book'}


#create data frame that has the result of the MDS plus the cluster numbers and titles
df = pd.DataFrame(dict(x=xs, y=ys, label=EM_label)) 

#group by cluster
groups = df.groupby('label')


# set up plot
fig, ax = plt.subplots(figsize=(8, 5)) # set size
ax.margins(0.05) # Optional, just adds 5% padding to the autoscaling

#iterate through groups to layer the plot
for name, group in groups:
    ax.plot(group.x, group.y, marker='o', linestyle='', ms=12, 
            label=cluster_names[name], color=cluster_colors[name], 
            mec='none')
    ax.set_aspect('auto')
    ax.tick_params(\
        axis= 'x',          # changes apply to the x-axis
        which='both',      # both major and minor ticks are affected
        bottom='off',      # ticks along the bottom edge are off
        top='off',         # ticks along the top edge are off
        labelbottom='off')
    ax.tick_params(\
        axis= 'y',         # changes apply to the y-axis
        which='both',      # both major and minor ticks are affected
        left='off',      # ticks along the bottom edge are off
        top='off',         # ticks along the top edge are off
        labelleft='off')

ax.legend(numpoints=1)  #show legend with only 1 point  
plt.show() #show the plot
