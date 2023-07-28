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
    filename = processor.get_current_filename()
    
    with open(filename, "r") as f:
        reader = csv.reader(f)
        for firstLine in reader:
            year = firstLine[0]
            month = firstLine[1]
            header = [month + ' ' + year]
            # with open("date.csv", "w") as file:
            #     None
            # file.close    
            
            return header
    

    
# print(title())

def month_data():
    # filename = processor.get_current_filename()
    inputDate = title()[0]
    # print(date)
    split = inputDate.split(' ')
    # print(split[0])
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
        fp.close
    f.close
    
    return

month_data()
