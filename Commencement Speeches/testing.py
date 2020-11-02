import csv

with open('2005.txt','r') as speech:
    with open('2005_text.csv', 'w') as file:
        fields = ['Paragraph']
        csv_writer = csv.DictWriter(file, fieldnames = fields)
        temp = ''
        for line in speech:
            if len(temp) > 150:
                csv_writer.writerow({'Paragraph': temp})
                temp =''
            temp += line.strip() # '\n'
            

