from tkinter import *
from tkcalendar import Calendar

import processor
root = Tk()
scroll=Scrollbar(root)
scroll.pack(side=RIGHT, fill=Y)
root.geometry("500x700")
root.title("Budget Calendar")
root['bg'] = 'light cyan'

cal = Calendar(root, font="Arial 16", selectmode='day', year=2023, month=1, day=19, foreground="black", selectforeground="red")

#on GUI
Initial=Label(root, text="Submit transactions", bg='light cyan')
space=Label(root, text="                     ", bg='light cyan', fg='light cyan')

instruction1=Label(root, text="Enter date", bg='light cyan')
date=Entry(root, width=15)
instruction2=Label(root, text="Enter earnings", bg='light cyan')
income=Entry(root, width=15)
instruction3=Label(root, text="Enter spendings", bg='light cyan')
spent=Entry(root, width=15)

def transaction():
    one=date.get()
    two=income.get()
    three=spent.get()
    processor.insert(one, two, three)

submit=Button(root, text="Submit to file", command=transaction)

def anydate():
    picked = cal.get_date()
    output = processor.pulling(picked)
    result = Label(root, text=str(output), bg="light cyan")
    result.pack()

enter=Button(root, text= "Enter", command=anydate)

#row0
Initial.pack(padx=20, pady=20)
#row1
instruction1.pack()
date.pack()
date.insert(0, "m/d/yy")
space.pack()
#row2
instruction2.pack()
income.pack()
#row3
instruction3.pack()
spent.pack()
#row4
submit.pack(padx=20, pady=20)
#row5
cal.pack()
enter.pack(padx=20, pady=20)
#row6
root.mainloop()