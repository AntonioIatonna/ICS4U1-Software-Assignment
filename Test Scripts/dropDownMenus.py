from tkinter import *

def nothing():
    print("damn")

root = Tk()

#Creating the main menu
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

#Creating toolbar
toolbar = Frame(root, bg = "blue")

insertButton = Button(toolbar, text = "Insert Image", command = nothing)
insertButton.pack(side = LEFT, padx = 2, pady = 2)
printButton = Button(toolbar, text = "Print", command = nothing)
printButton.pack(side = LEFT, padx = 2, pady = 2)

toolbar.pack(side = TOP, fill = X)

#Creating status bar
status = Label(root, text = "Prepairing to do nothing...", bd = 1, relief = SUNKEN, anchor = W)
status.pack(side = BOTTOM, fill = X)

root.mainloop()