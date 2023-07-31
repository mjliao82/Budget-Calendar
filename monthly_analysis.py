import csv
import processor



num_to_month = {
    '01':'Jan',
    '02':'Feb',
    '03':'Mar',
    '04':'Apr',
    '05':'May',
    '06':'Jun',
    '07':'Jul',
    '08':'Aug',
    '09':'Sep',
    '10':'Oct',
    '11':'Nov',
    '12':'Dec'
}


def title():
    # Read data from date.csv
    with open('date.csv', "r") as f:
        reader = csv.reader(f)
        for firstLine in reader:
            year = firstLine[0]
            month = firstLine[1]
            header = [month + ' ' + year]
    with open('last_date.csv', "w", newline='') as lf:
        writer = csv.writer(lf)
        writer.writerow(header)
    open('date.csv', 'w').close()
            


def month_data():
    filename = processor.get_current_filename()
    #print(filename)
    inputDate = []
    with open("last_date.csv", "r")as f:
        reader = csv.reader(f)
        for i in reader:
            inputDate = i
    inputMonth = ""
    inputYear = ""
    for i in inputDate:
        split = i.split(' ')
        inputMonth = split[0]
        inputYear = split[1]
    with open(filename, "r") as f:
        reader = csv.reader(f)
        next(reader)
        with open('temp.csv', "w", newline='\n') as fp:
            writer = csv.writer(fp)
            for line in reader:
                date = line[1].split('-')
                year = date[0]
                month = num_to_month.get(date[1])
                if inputYear == year and inputMonth == month:
                    print(line)
                    # print('yooo')
                    writer.writerow(line)
                else:
                    open('temp.csv', 'w').close()
        fp.close
    f.close
    return
    
#month_data()

def lines():
    num = 0
    with open("temp.csv", "r") as f:
        reader = csv.reader(f)
        for i in reader:
            num += 1 
    return num 
# print(lines())

def count_categories():
    dic={}
    with open("temp.csv", 'r') as f:
        reader = csv.reader(f)
        for i in reader:
            comma = i[0].split(';')
            if len(comma[2]) != 11:
                category = slice(11, len(comma[2]))
                category = comma[2][category]
                if dic.get(category)==None:
                    dic[category]=1
                else:
                    dic[category]+=1
            else:
                if dic.get("undefined")==None:
                    dic["undefined"]=1
                else:
                    dic["undefined"]+=1
    f.close()
    return dic 
# print(count_categories())

def labels():
    dic = count_categories()
    result = []
    for i in dic.keys():
        result.append(i)
    return result

def values():
    dic = count_categories()
    result = []
    for i in dic.values():
        result.append(i)
    return result

def income():
    result = []
    with open("temp.csv", 'r') as f:
        reader = csv.reader(f)
        for i in reader:
            line = i[0].split(";")
            in_obj = slice(7, len(line[0]))
            income = line[0][in_obj]
            income = income.strip()
            if income == "":
                income = "0"
            income = int(income)
            result.append(income)
    return result
# print(income())

def spending():
    result = []
    with open("temp.csv", "r") as f:
        reader = csv.reader(f)
        for i in reader:
            line = i[0].split(";")
            spe_obj = slice(12, len(line[1]))
            spending = line[1][spe_obj]
            spending = spending.strip()
            if spending == "":
                spending = "0"
            spending = int(spending)
            result.append(spending)
    return result

def default_label():
    result = []
    with open("temp.csv", "r") as f:
        reader = csv.reader(f)
        for i in reader: 
            result.append(i[1])
    return result