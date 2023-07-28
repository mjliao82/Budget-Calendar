import csv
import processor



num_to_month = {
    '01':'January',
    '02':'February',
    '03':'March',
    '04':'April',
    '05':'May',
    '06':'June',
    '07':'July',
    '08':'August',
    '09':'September',
    '10':'October',
    '11':'November',
    '12':'December'
}


def title():
    # filename = processor.get_current_filename()
    
    with open("date.csv", "r") as f:
        reader = csv.reader(f)
        for firstLine in reader:
            year = firstLine[0]
            month = firstLine[1]
            print(year)
            # line = 
            # print(line)
            header = [month + ' ' + year]
            with open("date.csv", "w") as file:
                None
            file.close    
            
            return header
    

    
            
    
print(title())



def month_data(inputYear, inputMonth):
    # filename = processor.get_current_filename()
    with open("events.csv", "r") as f:
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
    return

month_data("2023", "07")