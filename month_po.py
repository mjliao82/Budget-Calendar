import processor
import csv


#default layout of the imbedded page
def get_lines():
    filename = processor.get_current_filename()
    num = 0 
    with open(filename, "r") as f:
        reader = csv.reader(f)
        next(reader)
        for i in reader:
            num += 1 
    return num 
#print(get_lines())

def count_cate():
    filename = processor.get_current_filename()
    dic={}
    with open(filename, "r") as f:
        reader = csv.reader(f)
        next(reader)
        for i in reader:
            comma = i[0].split(";")
            if len(comma[2])!= 11: #categoy is filled
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
#print(count_cate())

def labels():
    dic = count_cate()
    result = []
    for i in dic.keys():
        result.append(i)
    return result

def values():    
    dic = count_cate()
    result = []
    for i in dic.values():
        result.append(i)
    return result 

def default_income():   #returns income in list
    filename = processor.get_current_filename()
    result = []
    with open(filename, "r")as f:
        reader = csv.reader(f)
        next(reader)
        for i in reader:
            deli = i[0].split(";")
            in_obj = slice(7, len(deli[0]))
            income = deli[0][in_obj]
            income = income.strip()
            if income == "":
                income = "0"
            income = int(income)
            result.append(income)
    return result
#print(default_income())

def default_spending():
    filename = processor.get_current_filename()
    result = []
    with open(filename, "r")as f:
        reader = csv.reader(f)
        next(reader)
        for i in reader:
            deli = i[0].split(";")
            spe_obj = slice(12, len(deli[1]))
            spending = deli[1][spe_obj]
            spending = spending.strip()
            if spending == "":
                spending = "0"
            spending = int(spending)
            result.append(spending)
    return result

def default_label():
    filename = processor.get_current_filename()
    result = []
    with open(filename, "r")as f:
        reader = csv.reader(f)
        next(reader)
        for i in reader:
            result.append(i[1])
    return result
#print(default_label())