#monthly analysis

import csv

def month_income(filename):
    with open(filename, 'r') as f:
        reader = csv.reader(f)
        # for line in reader:
        #     for 
        #     print(line[1])

#print("poop")
month_income("data.csv")