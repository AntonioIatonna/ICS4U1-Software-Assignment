from tkinter import *

#tickets = [[1, 2, 3, 4, 5, 6][7, 8, 9, 10, 11, 12]]

root = Tk() # Create graphics window
root.title("Lotto 6/49")
root.grid_columnconfigure(1, weight = 20, uniform = "key")
#root.grid_rowconfigure(1, weight = 0, uniform = "key")

# Create frames
terminalText = Frame(root, bg = "blue")
terminalText.grid(row = 10, columnspan = 10)
inputs = Frame(root)

# Create listboxes
userArrays = Listbox(root, height = 6)
userArrays.configure(justify = "center")
userArrays.grid(row = 2, column = 0, padx = 10, sticky = N)

cpuArray = Listbox(root, height = 1)
cpuArray.configure(justify = "center")
cpuArray.grid(row = 2, column = 10, padx = 10, sticky = N)

# Create starting labels
label_1 = Label(root, text = "User Tickets", font = "Verdana 8 bold")
label_1.grid(row = 1, column = 0)

label_2 = Label(root, text = "Winning Ticket", font = "Verdana 8 bold")
label_2.grid(row = 1, column = 10)

label_3 = Label(root, text = "Enter Inputs")
label_3.grid(row = 4, column = 0, columnspan = 11)

label_terminal = Label(root, bg = "blue", fg = "white", text = "Obama")
label_terminal.grid(row = 10, columnspan = 11, pady = 10)

#Creating Entrys
userInput = Entry(root)
userInput.configure(justify = "center")
userInput.grid(row = 5, column = 0, pady = 5, columnspan = 11)

uInput = userInput.get()
username = uInput
print(username)

# Insert each user ticket into listbox
#userArrays.insert(END, tickets[x])

root.mainloop()