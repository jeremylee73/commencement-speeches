import csv

with open('2008.txt','r') as speech:
    with open('2008_text.csv', 'w') as file:
        fields = ['Paragraph']
        csv_writer = csv.DictWriter(file, fieldnames = fields)
        for line in speech:
            line = line.strip() # '\n'
            csv_writer.writerow({'Paragraph': line})

