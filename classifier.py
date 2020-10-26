from textblob.classifiers import NaiveBayesClassifier
import nltk
import csv
import re
from nltk.corpus import stopwords 
import random

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
        block = re.findall(">[^\n\n]",data[i][0])
        if block : 
            data[i][0] = data[i][0].replace(block[0],"")
        
        mentions = re.findall("@\S+",data[i][0])
        if mentions : 
            for mention in mentions : 
                data[i][0] = data[i][0].replace(mention, "")
        
        links = re.findall("http[\S]+", data[i][0])
        if links :
            for link in links : 
                data[i][0] = data[i][0].replace(link, "")


        words = data[i][0].split()
        words = list(map( lambda x: x.lower(),words))
        words = list(filter( lambda x: x not in  stp ,words))
        words = list(filter( lambda x: x.isalnum() ,words))
        words = list(map( lambda x: x.strip(),words))
        words = list(filter( lambda x: len(x)>0 ,words))
        data[i][0] = " ".join(words)
    return data



def norm(text):

    words = text.split()
    words = list(map( lambda x: x.lower(),words))
    words = list(filter( lambda x: x not in  stp ,words))
    words = list(filter( lambda x: x.isalnum() ,words))
    words = list(map( lambda x: x.strip(),words))
    words = list(filter( lambda x: len(x)>0 ,words))
    text = " ".join(words)
    return text
    

            

data = load_data_into_mem()
random.shuffle(data)
all_data = normalize_data(data)
all_data = [z for z in all_data if z[1] == "yes" or len(z[0]) > 50]
train = all_data[:int(0.9*len(all_data))]
test = all_data[int(0.9*len(all_data)):]
classi = NaiveBayesClassifier(train)
print(classi.accuracy(test))
