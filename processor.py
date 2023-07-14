import csv


def row_delete(filename, row_num):
    with open(filename, 'r') as f:
        reader = csv.reader(f)
        lines = list(reader)
        del lines[row_num]
    with open(filename, 'w', newline = '') as file:
        writer = csv.writer(file)
        writer.writerow(lines)

print("fart")