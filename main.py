import os
import re

def main():
    """Writes all file names into files and files_ts"""
    files = []
    files_ts = []
    for i in range(2000,2021):
        files.append(str(i) + ".txt")
        files_ts.append(str(i) + "_TIMESTAMPED.txt")

    """Loads files into dictionary"""
    f_dict = {}
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
    wordcount_dict = {}
    for key in f_dict:
        if (f_dict[key][0] + f_dict[key][1] + f_dict[key][2] != "notranscriptfound"):
            for word in f_dict[key]:
                if (word not in wordcount_dict):
                    wordcount_dict[word] = 1
                else:
                    wordcount_dict[word] += 1

    """Prints ordered list of most used words"""
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
