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

#row_delete("events.csv", 40000)
#Income: 500; Spendings: 30; Category: Groceries; Description: ; 4,2023-07-18
#cleans up unfilled boxes
def janitor(filename):
    return #Lucas 