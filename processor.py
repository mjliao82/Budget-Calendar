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

print(get_current_filename())




#cleans up unfilled boxes
def janitor(filename):
    return #Lucas 