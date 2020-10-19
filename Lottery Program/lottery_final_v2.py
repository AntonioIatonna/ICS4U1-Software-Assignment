from tkinter import *
import time
import random

tickets = []
cpuTicket = []
matches = []
printTickets = []
printResults = []
tFrames = []
rFrames = []

# Begin Code
# Get user ticket quantity
print("Welcome to Lotto 6/49!\nPlease choose how many tickets you would like to play...")
while True:
    try:
        ticketNumber = int(input())
        break
    except:
        print("Please input a valid number!")

# Graphics window setup begins
# Create graphics window and set essential configurations
root = Tk() 
root.title("Lotto 6/49")
root.grid_columnconfigure(1, weight = 20, uniform = "key")

# Creating Frames
instructions = LabelFrame(root, text = "Instructions", padx = 20, pady = 5)
instructions.grid(row = 0, column = 5, columnspan = 11)

winningTicket = LabelFrame(root, text = "Winning Lottery Numbers", padx = 10, pady = 10)
winningTicket.grid(row = 10, column = 5, columnspan = 11)

for o in range(ticketNumber):
    ticketFrames = LabelFrame(root, text = "Ticket " + str((o + 1)))
    ticketFrames.grid(row = o + 2, column = 0, padx = 20)
    tFrames.append(ticketFrames)

    resultFrames = LabelFrame(root, text = "Ticket " + str((o + 1)))
    resultFrames.grid(row = o + 2, column = 100, padx = 20)
    rFrames.append(resultFrames)

# Create starting labels
label_1 = Label(root, text = "User Tickets", font = "Verdana 8 bold")
label_1.grid(row = 1, column = 0)

label_2 = Label(root, text = "User Results", font = "Verdana 8 bold")
label_2.grid(row = 1, column = 100)

label_3 = Label(root, text = "Winning Lottery Numbers", font = "Verdana 8 bold")
label_3.grid(row = 9, column = 5, columnspan = 11)

label_terminal = Label(instructions, text = "", width = 55, height = 2)
label_terminal.grid(row = 0, column = 5)

label_winning = Label(winningTicket, text = "", width = 30)
label_winning.grid(row = 0, column = 5)

for g in range(ticketNumber):
        ticket_label = Label(tFrames[g], text = "", width = 24)
        ticket_label.grid(row = g, column = 0, padx = 20, pady = 5)
        printTickets.append(ticket_label)

        result_label = Label(rFrames[g], text = "", width = 24)
        result_label.grid(row = g, column = 100, padx = 20, pady = 5)
        printResults.append(result_label)

# Graphics window setup ends

# Remainder of code begins
# configures 2d array for number of tickets and numbers for each ticket
tickets = [0] * ticketNumber
for i in range(ticketNumber):
    tickets[i] = [0] * 6
# configures array for cpu ticket
cpuTicket = [0] * 6

# recieves user input for the numbers on each ticket
for x in range(ticketNumber):
    for y in range(6):
        label_terminal.configure(text = "Please select your numbers for ticket " + str(x + 1) + "...\nPlease select number " + str(y + 1))
        while True: 
            try:
                num = int(input())
                for t in range(6):
                    while(num == tickets[x][t] or num > 49):
                        label_terminal.configure(text = "Number is already in use on this ticket or is greater than 49! Pick again.")
                        num = int(input())
                break
            except:
                label_terminal.configure(text = "Please enter a valid number!")
        tickets[x][y] = num       
    # sort each ticket
    for j in range(6):
        for k in range(j + 1, 6):
            if(tickets[x][j] > tickets[x][k]):
                temp = tickets[x][j]
                tickets[x][j] = tickets[x][k]
                tickets[x][k] = temp
    
    printTickets[x].configure(text = tickets[x])

# generate and sort winning ticket and check far and replace duplicate numbers
for m in range(6):
    num = random.randint(1, 49)
    for n in range(6):
        while(num == cpuTicket[n]):
            num = random.randint(1, 49)
    cpuTicket[m] = num    
# sort cpu ticket
for a in range(6):
    for b in range(a + 1, 6):
        if(cpuTicket[a] > cpuTicket[b]):
            temp = cpuTicket[a]
            cpuTicket[a] = cpuTicket[b]
            cpuTicket[b] = temp

label_winning.configure(text = cpuTicket)

# compare all user tickets to winning ticket
label_terminal.configure(text = "Checking user tickets...")
for w in range(ticketNumber):
    userMatch = 0
    for z in range(6):
        for v in range(6):
            if(tickets[w][z] == cpuTicket[v]):
                userMatch +=1
    matches.append(userMatch)

# check if user won and print result
for u in range(ticketNumber):
    if(matches[u] >= 3):
        printResults[u].configure(text = "Winner! " + str(matches[u]) + " numbers matched!")
    else:
        printResults[u].configure(text = "You Lost! " + str(matches[u]) + " numbers matched.")
    time.sleep(2)

label_terminal.configure(text = "Results...")
root.mainloop() # Keep window on screen