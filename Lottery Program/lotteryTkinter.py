from tkinter import *
import time
import random

tickets = []
cpuTicket = []
matches = []
terminalText = ""
# entryData = ""

root = Tk() # Create graphics window and set essential configurations
root.title("Lotto 6/49")
root.grid_columnconfigure(1, weight = 20, uniform = "key")

# Create listboxes
userList = Listbox(root, height = 6)
userList.configure(justify = "center")
userList.grid(row = 2, column = 0, padx = 10, sticky = N)

cpuList = Listbox(root, height = 1)
cpuList.configure(justify = "center")
cpuList.grid(row = 2, column = 10, padx = 10, sticky = N)

# Create starting labels
label_1 = Label(root, text = "User Tickets", font = "Verdana 8 bold")
label_1.grid(row = 1, column = 0)

label_2 = Label(root, text = "Winning Ticket", font = "Verdana 8 bold")
label_2.grid(row = 1, column = 10)

label_3 = Label(root, text = "Enter Inputs")
label_3.grid(row = 4, column = 0, columnspan = 11)

label_terminal = Label(root, text = terminalText)
label_terminal.grid(row = 10, columnspan = 11, pady = 10)

# Begin Code
label_terminal.configure(text = "Welcome to Lotto 6/49!\nPlease choose how many tickets you would like to play...")
while(True):
    try:
        ticketNumber = int(input())
        break
    except:
        label_terminal.configure(text = "Please input a valid number!")
    
# sets up 2d array for number of tickets and numbers for each ticket
tickets = [0] * ticketNumber
for i in range(ticketNumber):
    tickets[i] = [0] * 6
# configures array for cpu ticket
cpuTicket = [0] * 6

# recieves user input for the numbers on each ticket
for x in range(ticketNumber):
    label_terminal.configure(text = "Please select your numbers for ticket " + str(x + 1))
    for y in range(6):
        label_terminal.configure(text = "Please select number " + str(y + 1))
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

    # Insert each user ticket into listbox
    userList.insert(END, tickets[x])

# generate and sort winning ticket and check and replace duplicate numbers
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

cpuList.insert(END, cpuTicket)

# compare all user tickets to winning ticket
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
        label_terminal.configure(text = "Congratulations! You won on ticket " + str(u + 1) + " with " + str(matches[u]) + " numbers!")
    else:
        label_terminal.configure(text = "Sorry. You did not win on ticket " + str(u + 1) + " with only " + str(matches[u]) + " numbers matching.")
    time.sleep(2)

root.mainloop() # Keep window on screen