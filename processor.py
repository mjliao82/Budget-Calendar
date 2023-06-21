import csv
from time import strptime
import calendar
import pandas as pd

#wrting csv, putting in date, money earned and money spent
header = ["Date", "Money Earned", "Money Spent"]
def insert(date, earned, spent): #input
    with open("data.csv") as r:
        with open("data.csv", "a", newline = "") as f:
            reader = csv.reader(r)
            writer = csv.writer(f)
            if header not in reader:
                writer.writerow(header)
            writer.writerow([date, earned, spent])
    f.close()
    return None


#read file and return money spent and earned based on input date

def pulling(date):
    earned = 0
    spent = 0
    with open("data.csv") as f:
        reader = csv.reader(f)
        next(reader)
        for line in reader:
            if line[0] == date:
                earned += int(line[1])
                spent += int(line[2])
    first = ("On" + ' ' + date + ":")
    second = ("     earned:" + " " + str(earned))
    third = ("     spent:" + " " + str(spent))
    return first + second + third


monthToInt = {
    "jan" : 1,
    "feb" : 2,
}
#total month's earning and spending
def monthTotal(month):
    totalEarned = 0
    totalSpent = 0
    monthnum = monthToInt[month]
    with open("data.csv") as r:
        reader = csv.reader(r)
        next(reader)
        for line in reader:
            mdy = line[0].split("/")
            mth = mdy[0]
            yr = mdy[2]
            while mth == monthnum:
                totalEarned += line[1]
                totalSpent += line[2]
    statement = ("For the month of " + month + ", you earned:" + str(totalEarned) + " and spent:" + str(totalEarned))
    return statement