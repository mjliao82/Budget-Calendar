from tkinter import *

import main
root = Tk()

root.title("Budget Calendar")
def jan1203():
    output = main.pulling("01/12/2023")
    result = Label(root, text=str(output))
    result.grid(row=8, column=0, columnspan=4)
    return None

#on GUI
Initial=Label(root, text="Enter your transaction")
space=Label(root, text="                     ")
month=Label(root, text="January 2023")
twelve=Button(root, text="12th", command=jan1203)
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
space.grid(row=5, column=0)
#row6
month.grid(row=6, column=0, columnspan=4)
twelve.grid(row=7, column=0, columnspan=4)
space.grid(row=8, column=0, padx=40, pady=40)
root.mainloop()