'''
number of lines in the calenar 
calculate percentage of what each possibnle categories are
we can make a pie chart outa it
monthly accumulation 
potentially a line chart on any "year" clicked for growth over the months
'''
import processor
import os
import csv
import plotly.io as pio
import plotly.graph_objects as go

#default layout of the imbedded page
def get_lines():
    filename = processor.get_current_filename()
    num = 0 
    with open(filename, "r") as f:
        reader = csv.reader(f)
        next(reader)
        for i in reader:
            num += 1 
    return num 
#print(get_lines())

def count_cate():
    filename = processor.get_current_filename()
    dic={}
    with open(filename, "r") as f:
        reader = csv.reader(f)
        next(reader)
        for i in reader:
            comma = i[0].split(";")
            if len(comma[2])!= 11: #categoy is filled
                category = slice(11, len(comma[2]))
                category = comma[2][category]
                if dic.get(category)==None:
                    dic[category]=1
                else:
                    dic[category]+=1
            else:
                if dic.get("undefined")==None:
                    dic["undefined"]=1
                else:
                    dic["undefined"]+=1
    f.close()
    return dic 
#print(count_cate())

def labels():
    dic = count_cate()
    result = []
    for i in dic.keys():
        result.append(i)
    return result

def values():    
    dic = count_cate()
    result = []
    for i in dic.values():
        result.append(i)
    return result 

def update():
    fig = go.Figure(data=[go.Pie(labels=labels(), values=values(), textinfo='label+percent',insidetextorientation='radial')])
    pio.write_html(fig, 'templates/monthEmbed.html')
    return 