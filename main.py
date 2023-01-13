import csv

#wrting csv, putting in date, money earned and money spent
header = ["Date", "Money Earned", "Money Spent"]
def insert(date, earned, spent): #input
    with open("data.csv") as r:
        with open("data.csv", "a") as f:
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
        reader=csv.reader(f)
        next(reader)
        for line in reader:
            if date==line[0]:
                earned += int(line[1])
                spent += int(line[2])
    print("On" + ' ' + date + ":")
    print("     earned:" + " " + str(earned))
    print("     spent:" + " " + str(spent))
    print("hello1")
    return None

#insert("01/12/2023", "10", "20")
pulling("01/12/2023")