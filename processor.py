import csv
import os

def load_id():
    if os.path.exists('id.txt'):
        with open('id.txt', 'r') as f:
            return int(f.read())
    else:
        return 0

def save_id(id):
    with open('id.txt', 'w') as f:
        f.write(str(id))

def IDs(event):
    id = load_id()
    title = event['title']
    add = title + ("; ") + str(id) 
    id += 1
    save_id(id)
    event['title'] = add
    return event

def row_delete(filename, id):
    with open(filename, 'r') as f:
        reader = csv.reader(f)
        lines = list(reader)
        index = 0
        for line in lines:
            if index == 0:
                index+=1
            else:
                sub = line[0]
                deli = sub.split(";")
                if deli[4].strip()==str(id):
                    lines.remove(line)
    with open(filename, 'w', newline = '') as file:
        writer = csv.writer(file)
        for line in lines:
            writer.writerow(line)

def get_current_filename():
    with open('current_file.txt', 'r') as f:
        filename = f.read().strip()
        filename=filename.replace(" ", "_")
        filename = filename+str(".csv")
        if filename == "Main_Calendar.csv":
            return 'events.csv'
        if not os.path.exists(filename):
            with open(filename, "w") as r:
                writer = csv.writer(r)
                writer.writerow(['title', 'start'])
    return filename

def file_size(file):
    with open(file, 'r') as f:
        num_lines = sum(1 for line in f)
        return num_lines
def cumalative():
    file_sort()
    with open("data.csv", "w") as reset:
        writer = csv.writer(reset)
        writer.writerow(['title', 'start'])
    reset.close()
    filename = get_current_filename()
    income = 0
    spending = 0
    count = 0
    length = file_size(filename)
    with open(filename, "r") as f:
        reader = csv.reader(f)
        next(reader) 
        count += 1
        temp=""
        first_iter = True
        for i in reader:
            deli = i[0].split(";")
            if i[1]!=temp: #i[1] is the date
                if first_iter==False:   
                    with open("data.csv", "a") as mid:
                        writer = csv.writer(mid)
                        writer.writerow(["Income: "+str(income), temp]) 
                        writer.writerow(["Spending: "+str(spending), temp])
                    mid.close()
                first_iter=False
                temp = i[1]
                income = 0
                spending = 0
            if i[1]==temp:
                in_obj=slice(7, len(deli[0]))
                temp_in_str = deli[0][in_obj]
                spe_obj=slice(12, len(deli[1]))
                temp_spe_str = deli[1][spe_obj]
                temp_in_str = temp_in_str.strip()
                if temp_in_str == "":
                    temp_in_str = "0"
                temp_spe_str = temp_spe_str.strip()
                if temp_spe_str == "":
                    temp_spe_str = "0"
                temp_income = int(temp_in_str)
                temp_spending = int(temp_spe_str)
                income += temp_income
                spending += temp_spending
            count+=1
            if count == length: #last date case
                with open("data.csv", "a") as last:
                    writer = csv.writer(last)
                    writer.writerow(["Income: "+str(income), i[1]])
                    writer.writerow(["Spending: "+str(spending), i[1]])
                last.close()
    return 
#cumalative()

def file_sort():
    filename = get_current_filename()
    with open(filename, "r")as f:
        reader = csv.reader(f)
        next(reader)
        lines = list(reader)
        saver = {}  #reduce runtime for get or else method
        ref = []
        cur = ""
        for line in lines:
            cur = line[1]
            #print(cur)
            if saver.get(cur, -5)==-5:
                saver[cur]=1
            else:
                saver[cur]+=1
            if saver[cur]==1:
                ref.append(line[1])
        with open(filename, "w")as header:
            writer = csv.writer(header)
            writer.writerow(['title', 'start'])
        header.close()
        with open(filename, "a") as f:
            writer = csv.writer(f)
            i = 0 
            while i < len(ref):
                for line in lines:
                    if line[1]==ref[i]:
                        writer.writerow(line)
                i+=1
        f.close()
    return
# file_sort()

#cleans up unfilled boxes
def janitor(filename):
    return #Lucas 


