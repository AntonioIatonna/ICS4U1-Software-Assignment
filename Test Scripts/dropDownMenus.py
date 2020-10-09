from tkinter import *

def nothing():
    print("damn")

root = Tk()

myMenu = Menu(root)
root.config(menu = myMenu)

fileMenu = Menu(myMenu)
myMenu.add_cascade(label = "File", menu = fileMenu)
fileMenu.add_command(label = "New Project...", command = nothing)
fileMenu.add_checkbutton(label = "New...", command = nothing)
fileMenu.add_separator()
fileMenu.add_command(label = "Exit", command = nothing)

editMenu = Menu(myMenu)
myMenu.add_cascade(label = "Edit", menu = editMenu)
editMenu.add_command(label = "Redo", command = nothing)

root.mainloop()