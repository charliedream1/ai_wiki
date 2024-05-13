#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 27 17:34:06 2019

@author: Preeti
"""
#importing methods from other files 
from Clustering_BOW_Kmeans import bow_kmeans
from Clustering_BOW_EM import bow_EM
from Clustering_BOW_HC import bow_hc


#importing libraries 
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





#Data preparation and preprocess
def custom_preprocessor(text):
        text = re.sub(r'\W+|\d+|_', ' ', text)    #removing numbers and punctuations
        text =  re.sub(r'\s+',' ',text) #remove multiple spaces into a single space
        text = re.sub(r"\s+[a-zA-Z]\s+",' ',text) #remove a single character
        text = text.lower() 
        text = nltk.word_tokenize(text)       #tokenizing
        text = [word for word in text if not word in stop_words] #English Stopwords
        #text = [lemmatizer.lemmatize(word) for word in text]              #Lemmatising
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


# Data transformation BOW
# Creating the BOW model
from sklearn.feature_extraction.text import CountVectorizer
vectorizer = CountVectorizer(max_features=2000, min_df=3, max_df=0.6)
X = vectorizer.fit_transform(docs)
X.toarray()


#**************************comparing KMeans and EM*****************************
num_cluster = 3
Kmeans_labels = bow_kmeans(X, k = num_cluster)
#print(len(Kmeans_labels))
EM_labels = bow_EM(X)
#print(len(EM_labels))


print('Kappa for KMeans and EM:',metrics.cohen_kappa_score(Kmeans_labels,EM_labels,weights='linear'))

#**************************comparing KMeans and HC*****************************
num_cluster = 3
Kmeans_labels = bow_kmeans(X, k = num_cluster)
#print(len(Kmeans_labels))
HC_labels = bow_hc(X,k = num_cluster )
#print(len(HC_labels))


print('Kappa for KMeans and HC:',metrics.cohen_kappa_score(Kmeans_labels,HC_labels,weights='linear'))

#**************************comparing EM and HC*********************************
num_cluster = 3
EM_labels = bow_EM(X)
#print(len(EM_labels))
HC_labels = bow_hc(X, k = num_cluster)
#print(len(HC_labels))

print('Kappa for EM and HC:',metrics.cohen_kappa_score(EM_labels,HC_labels,weights='linear'))
