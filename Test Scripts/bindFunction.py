from tkinter import *

root = Tk()

def printName():
    print("Hello World")

button_1 = Button(root, text = "Print Text", command = printName)
button_1.grid(row = 0, column = 0)

root.mainloop()