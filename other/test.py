import csv

def to_wordlist(directory,file):
    non_let = ['(',')','"','`','.',',','!','?']
    with open(directory+'/'+file,'r') as f:
        words = [line.strip().split(" ") for line in f]
        w=[]
        for wlis in words:
            w += wlis
        w_final = []
        for i in w:
            if i == ' ' or i =='':
                pass
            else:
                i_low = i.lower()
                for non_char in non_let:
                    i_low = i_low.replace(non_char,'')
                if '--' in i_low:
                    a,b = i_low.split('--')
                    w_final.append(a)
                    w_final.append(b)
                else:
                    w_final.append(i_low)
                    
    return w_final
                   

def main():
    yearstemp = [f'{i}' for i in range(2000,2021)]
    year_ts = [i+'_TIMESTAMPED.txt' for i in yearstemp]
    year  = [i+'.txt' for i in yearstemp]
    comdir = "../Commencement Speeches"
    col = ["Word","Frequency"]
    for yr in year:
        wlist = to_wordlist(comdir,yr)
        wdict = {}
        for word in wlist:
            if word in wdict:
                wdict[word]+=1
            else:
                wdict[word]=1
        
            csv_file = f'{yr}.csv'
            with open(csv_file,'w') as cv:
                write = csv.DictWriter(cv,fieldnames=col)
                write.writeheader()
                for i in wdict:
                    tempdic = {"Word":i, "Frequency":wdict[i]}
                    write.writerow(tempdic)
    


if __name__ == "__main__":
    main()

    
