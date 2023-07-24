'''
number of lines in the calenar 
calculate percentage of what each possibnle categories are
we can make a pie chart outa it
monthly accumulation 
potentially a line chart on any "year" clicked for growth over the months
'''
import processor
import csv


def get_lines(filename):
    filename = processor.get_current_filename()
    num = 0 
    with open(filename, "r") as f:
        reader = csv.reader(f)
        for i in reader:
            num += 1 
    return num 

def count_cate():
    filename = processor.get_current_filename()
    dic={}
    with open(filename, "r") as f:
        reader = csv.reader(f)
        next(reader)
        for i in reader:
            comma = i[0].split(";")
            print(comma[2])
            if len(comma[2])!= 11: #categoy is filled
                category = slice(11, len(comma[2]))
                category = comma[2][category]
                if dic.get(category)==None:
                    dic[category]=1
                else:
                    dic[category]+=1
                    #dic[category]+=1
    return dic 
print(count_cate())