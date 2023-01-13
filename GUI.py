from tkinter import *

import main
root = Tk()

def jan1203():
    output = main.pulling("01/12/2023")
    result = Label(root, text=str(output))
    result.pack()
    return None

#on GUI
myLabel = Label(root, text="Budget Calendar")
month=Label(root, text="January 2023")
myButton=Button(root, text="12th", command=jan1203)
myLabel.pack()
month.pack()
myButton.pack()
root.mainloop()