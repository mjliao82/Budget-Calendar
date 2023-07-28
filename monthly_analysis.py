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
    with open("date.csv", "r") as f:
        reader = csv.reader(f)
        for firstLine in reader:
            year = firstLine[0]
            month = firstLine[1]
            header = [month + ' ' + year]
            with open("date.csv", "w") as file:
                None
            file.close
            return header
        
['2023,Mar']
def month_data():
    time = title()[0]
    print(time)
    split = time.split(' ')
    print(split[0])
    '''
    filename = processor.get_current_filename()
    with open(filename, "r") as f:
        reader = csv.reader(f)
        next(reader)
        for line in reader:
            date = line[1].split('-')
            year = date[0]
            month = date[1]
            with open('temp.csv', "a") as fp:
                writer = csv.writer(fp)
                if inputYear == year and inputMonth == month:
                    writer.writerow(line)
    '''
    return
month_data()