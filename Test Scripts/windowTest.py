from tkinter import *

root = Tk() #Create graphics window

#Create frames
topFrame = Frame(root)
topFrame.pack(side = TOP)
bottomFrame = Frame(root)
bottomFrame.pack(side = BOTTOM)

#Create widgets / buttons
button1 = Button(topFrame, text = "Button 1", fg = "red")
button2 = Button(topFrame, text = "Button 2", fg = "blue")
button3 = Button(topFrame, text = "Button 3", fg = "green")
button4 = Button(bottomFrame, text = "Button 4", fg = "purple")

#display widgets
button1.pack(side = LEFT)
button2.pack(side = LEFT)
button3.pack(side = LEFT)
button4.pack(side = BOTTOM)

root.mainloop() #Keep window on screen