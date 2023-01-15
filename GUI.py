from tkinter import *

import main
root = Tk()

root.title("Budget Calendar")
def jan1203():
    output = main.pulling("01/12/2023")
    result = Label(root, text=str(output))
    result.pack()
    return None

#on GUI
Initial=Label(root, text="Enter your transaction")
space=Label(root, text="                     ")
month=Label(root, text="January 2023")
twelve=Button(root, text="12th", command=jan1203)
date=Entry(root, width=30)
income=Entry(root, width=30)
spent=Entry(root, width=30)





Initial.pack()
date.pack()
date.insert(0, "ex: '01/12/2023'")
income.pack()
income.insert(1, "ex: '10'")
spent.pack()
spent.insert(2, "ex: '20'")
space.pack()
month.pack()
twelve.pack()
root.mainloop()