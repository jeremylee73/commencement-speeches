import os
import re
import csv
import numpy as np
import pandas as pd
from PIL import Image
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import matplotlib.pyplot as plt
import nltk
from nltk.corpus import stopwords

files = []
files_ts = []
f_dict = {}
wordcount_dict = {}

def main():
    """Writes all file names into files and files_ts"""
    for i in range(2000,2021):
        files.append(str(i) + ".txt")
        files_ts.append(str(i) + "_TIMESTAMPED.txt")

    """Loads files into dictionary"""
    for file in files:
        f_dict[file[slice(0,-4)]] = []
        path = os.getcwd() + "/Commencement Speeches/" + file
        with open(path, "r") as f:
            for line in f:
                # Cleans string
                pat = re.compile(r'[^a-zA-Z ]+')
                line = re.sub(pat, '', line).lower()
                # Splits string
                words = line.split()
                # Appends words into dictionary entry
                for word in words:
                    f_dict[file[slice(0,-4)]].append(word)
 
    for key in f_dict:
        if (f_dict[key][0] + f_dict[key][1] + f_dict[key][2] != "notranscriptfound"):
            temp={}
            for word in f_dict[key]:
                
                if (word not in temp):
                    temp[word] = 1
                    #wordcount_dict[word] = 1
                else:
                    temp[word] +=1
                    #wordcount_dict[word] += 1
            wordcount_dict[key] = temp


    
    '''
    """Writes words into words.csv"""
    with open("words.csv", mode = "w") as file:
        writer = csv.writer(file, delimiter = ",", quotechar = '"', quoting = csv.QUOTE_MINIMAL)
        writer.writerow(["word", "count"])
        for key in wordcount_dict:
            writer.writerow([key, str(wordcount_dict[key])])
    '''
    """Creates word cloud"""
    # update_wordcloud()

    """Prints ranked list of most used words"""
    directory = 'years/'
    col = ["Rank", "Word","Count"]
    # Prints the data into csv
    for file in files:
        file = file[slice(0,-4)]
        try:
            with open(directory + f'{file}.csv','w') as f:
                
                write = csv.DictWriter(f,fieldnames=col)
                write.writeheader()
                for i in print_ranks(wordcount_dict[file], 50):
                    write.writerow(i)
        except:
            pass
    
"""Updates wordcloud.png"""
def update_wordcloud():
    text = ""
    for key in wordcount_dict:
        for i in range(wordcount_dict[key]):
            text += key + " "
    wordcloud = WordCloud(width = 3000, height = 2000, random_state=1, background_color='salmon', colormap='Pastel1', collocations=False, stopwords = STOPWORDS).generate(text)
    wordcloud.to_file("wordcloud.png")

def filtering(word):
    '''quick function to eliminate bad words in order to use filter()'''
    if word in STOPWORDS:
        return False
    return True

"""Prints ordered list of most used words"""
def print_ranks(wordcount_dict,top):
    max = 0
    for key in wordcount_dict:
        if wordcount_dict[key] > max:
            if key not in STOPWORDS:
                max = wordcount_dict[key]
    count = 1

    rank_list=[]
    for i in range(max, 0, -1):
        for key in wordcount_dict:
            if wordcount_dict[key] == i:
                order = {'Rank':count, 'Word':key, 'Count': wordcount_dict[key]}
                #print(str(count) + ". " + key + " (count: " + str(wordcount_dict[key]) + ")")
                rank_list.append(order)
                count += 1
        if count >= top:
            break
    return rank_list
        
if __name__ == "__main__":
    main()
