import csv

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

#insert("01/12/2023", "10", "20")
print(pulling("01/12/2023"))