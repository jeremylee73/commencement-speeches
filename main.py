import os
import re
import csv
import numpy as np
import pandas as pd
from PIL import Image
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import matplotlib.pyplot as plt


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

    """Takes cumulative word counts and stores in dictionary"""
    for key in f_dict:
        if (f_dict[key][0] + f_dict[key][1] + f_dict[key][2] != "notranscriptfound"):
            for word in f_dict[key]:
                if (word not in wordcount_dict):
                    wordcount_dict[word] = 1
                else:
                    wordcount_dict[word] += 1

    """Writes words into words.csv"""
    with open("words.csv", mode = "w") as file:
        writer = csv.writer(file, delimiter = ",", quotechar = '"', quoting = csv.QUOTE_MINIMAL)
        writer.writerow(["word", "count"])
        for key in wordcount_dict:
            writer.writerow([key, str(wordcount_dict[key])])

    """Creates word cloud"""
    text = ""
    for key in wordcount_dict:
        for i in range(wordcount_dict[key]):
            text += key + " "
    wordcloud = WordCloud(width = 3000, height = 2000, random_state=1, background_color='salmon', colormap='Pastel1', collocations=False, stopwords = STOPWORDS).generate(text)
    wordcloud.to_file("wordcloud.png")

"""Prints ordered list of most used words"""
def print_ranks():
    max = 0
    for key in wordcount_dict:
        if wordcount_dict[key] > max:
            max = wordcount_dict[key]
    count = 1
    for i in range(max, 0, -1):
        for key in wordcount_dict:
            if wordcount_dict[key] == i:
                print(str(count) + ". " + key + " (count: " + str(wordcount_dict[key]) + ")")
                count += 1

if __name__ == "__main__":
    main()
