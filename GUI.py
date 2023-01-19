from tkinter import *
from tkcalendar import Calendar

import main
root = Tk()
root.geometry("500x500")
root.title("Budget Calendar")

cal = Calendar(root, font="Arial 16", selectmode='day', year=2023, month=1, day=19, foreground="BLACK", selectforeground="red")

#on GUI
Initial=Label(root, text="Enter your transaction")
space=Label(root, text="                     ")

instruction1=Label(root, text="Enter date")
date=Entry(root, width=15)
instruction2=Label(root, text="Enter earnings")
income=Entry(root, width=15)
instruction3=Label(root, text="Enter spendings")
spent=Entry(root, width=15)

def transaction():
    one="'"+date.get()+"'"
    two=income.get()
    three=spent.get()
    main.insert(one, two, three)

enter=Button(root, text="Enter", command=transaction)

#row0
Initial.grid(row=0, column=0, columnspan=4, padx=20, pady=10)
#row1
date.grid(row=1, column=1)
date.insert(0, "mm/dd/yyyy")
instruction1.grid(row=1, column=0)
#row2
income.grid(row=2, column=1)
instruction2.grid(row=2, column=0)
#row3
spent.grid(row=3, column=1)
instruction3.grid(row=3, column=0)
#row4
enter.grid(row=4, column=0, columnspan=4, padx=20, pady=20)
#row5
cal.grid(row=5, column=0, columnspan=6)
#row6
space.grid(row=8, column=0, padx=40, pady=40)
root.mainloop()