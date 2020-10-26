import csv
import random
import re

import nltk
from nltk.corpus import stopwords 
from textblob.classifiers import NaiveBayesClassifier

stp = set(stopwords.words('english')) 

def load_data_into_mem():
    data = []
    with open('final_dataset.csv') as f : 
        csv_file = csv.reader(f)
        for i in csv_file:
            data.append(i)
    return data

def normalize_data(data):
    for i in  range(len(data)) : 
        data[i][0] = sanitize_text(data[i][0])
    return data



def sanitize_text(text):
    block = re.findall(">[^\n\n]",text)
    if block : 
        text = text.replace(block[0],"")
    
    mentions = re.findall("@\S+",text)
    if mentions : 
        for mention in mentions : 
            text = text.replace(mention, "")
    
    links = re.findall("http[\S]+", text)
    if links :
        for link in links : 
            text = text.replace(link, "")

    words = text.split()
    words = list(map( lambda x: x.lower(),words))
    words = list(filter( lambda x: x not in  stp ,words))
    words = list(filter( lambda x: x.isalnum() ,words))
    words = list(map( lambda x: x.strip(),words))
    words = list(filter( lambda x: len(x)>0 ,words))
    text = " ".join(words)
    return text
    

def train_model():
    data = load_data_into_mem()
    random.shuffle(data)
    all_data = normalize_data(data)
    all_data = [z for z in all_data if z[1] == "yes" or len(z[0]) > 50]
    train = all_data[:int(0.9*len(all_data))]
    test = all_data[int(0.9*len(all_data)):]
    classi = NaiveBayesClassifier(train)
    print("Model has accuracy of " + str(classi.accuracy(test)*100) + "%")
