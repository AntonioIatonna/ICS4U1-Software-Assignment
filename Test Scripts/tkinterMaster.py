from tkinter import *
import time

ticketNumber = 6
tickets = [[1,2,3,4,5,6],[7,8,9,10,11,12],[1,2,3,4,5,6],[7,8,9,10,11,12],[1,2,3,4,5,6],[49,48,45,40,47,43]]
cpuTicket = [9, 18,19, 29, 39, 49]
printTickets = []
tFrames = []
rFrames = []

root = Tk() # Create graphics window
root.title("Lotto 6/49")
root.title("Lotto 6/49")
root.grid_columnconfigure(1, weight = 20, uniform = "key")

# Creating Frames
instructions = LabelFrame(root, text = "Instructions", padx = 20, pady = 5)
instructions.grid(row = 0, column = 5, columnspan = 11)

winningTicket = LabelFrame(root, text = "Winning Ticket", padx = 10, pady = 10)
winningTicket.grid(row = 10, column = 5, columnspan = 11)

for o in range(ticketNumber):
    ticketFrames = LabelFrame(root, text = "Ticket " + str((o + 1)))
    ticketFrames.grid(row = o + 2, column = 0, padx = 20)
    tFrames.append(ticketFrames)

    resultFrames = Frame(root)
    resultFrames.grid(row = o + 2, column = 10)
    rFrames.append(resultFrames)

# Create starting labels
label_1 = Label(root, text = "User Tickets", font = "Verdana 8 bold")
label_1.grid(row = 1, column = 0)

label_2 = Label(root, text = "User Results", font = "Verdana 8 bold")
label_2.grid(row = 1, column = 10)

label_3 = Label(root, text = "Winning Ticket", font = "Verdana 8 bold")
label_3.grid(row = 9, column = 5, columnspan = 11)

label_terminal = Label(instructions, text = "")
label_terminal.grid(row = 0, column = 5)

label_winning = Label(winningTicket, text = cpuTicket)
label_winning.grid(row = 0, column = 5)

for g in range(ticketNumber):
        ticket_label = Label(tFrames[g], text = tickets[g], width = 12)
        ticket_label.grid(row = g, column = 0, padx = 20, pady = 5)
        printTickets.append(ticket_label)


root.mainloop()