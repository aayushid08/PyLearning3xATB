import csv

with open('TD.csv') as csvfile:     # specially for csv
    reader = csv.reader(csvfile)
    for col in reader:
        print(col[0],col[1],sep=" | ")