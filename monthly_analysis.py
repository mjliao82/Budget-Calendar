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

# def title():
#     filename = processor.get_current_filename()
#     with open(filename, "r") as f:
#         reader = csv.reader(f)
#         next(reader)
#         for line in reader:
#             date = line[1].split('-')
#             year = date[0]
#             month = date[1]
#         header = [year + ' ' + num_to_month.get(month)]
            
#         # with open("temp.csv", "w") as fp:
#         #     writer = csv.writer(fp)
            
#         # print(header)
#     return header

# title()

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