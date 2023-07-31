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
    # filename = processor.get_current_filename()
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
    
    with open("events.csv", "r") as f:
        reader = csv.reader(f)
        next(reader)
        with open('temp.csv', "a", newline='\n') as fp:
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
    
month_data()
