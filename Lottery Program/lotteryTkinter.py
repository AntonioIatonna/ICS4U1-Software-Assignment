from tkinter import *
import time
import random

tickets = []
cpuTicket = []
matches = []

root = Tk() # Create graphics window

# Create frames

# Create listbox
userArrays = Listbox(root)
userArrays.configure(justify = "center")
userArrays.grid(row = 1, column = 0)

# Create starting labels
label_1 = Label(root, text = "User Tickets")
label_1.grid(row = 0, column = 0)

print("Welcome to Lotto 6/49!\nPlease choose how many tickets you would like to play...")
while True:
    try:
        ticketNumber = int(input())
        break
    except:
        print("Please input a valid number!")

# sets up 2d array for number of tickets and numbers for each ticket
tickets = [0] * ticketNumber
for i in range(ticketNumber):
    tickets[i] = [0] * 6
# configures array for cpu ticket
cpuTicket = [0] * 6

# recieves user input for the numbers on each ticket
for x in range(ticketNumber):
    print("Please select your numbers for ticket " + str(x + 1))
    for y in range(6):
        print("Please select number " + str(y + 1))
        while True: 
            try:
                num = int(input())
                for t in range(6):
                    while(num == tickets[x][t] or num > 49):
                        print("Number is already in use on this ticket or is greater than 49! Pick again.")
                        num = int(input())
                break
            except:
                print("Please enter a valid number!")
        tickets[x][y] = num        
    # sort each ticket
    for j in range(6):
        for k in range(j + 1, 6):
            if(tickets[x][j] > tickets[x][k]):
                temp = tickets[x][j]
                tickets[x][j] = tickets[x][k]
                tickets[x][k] = temp

    # Insert each user ticket into listbox
    userArrays.insert(END, tickets[x])

# generate and sort winning ticket and check and replace duplicate numbers
for m in range(6):
    num = random.randint(1, 49)
    for n in range(6):
        while(num == cpuTicket[n]):
            num = random.randint(1, 49)
    cpuTicket[m] = num    
#improve sort (sort as you go)
for a in range(6):
    for b in range(a + 1, 6):
        if(cpuTicket[a] > cpuTicket[b]):
            temp = cpuTicket[a]
            cpuTicket[a] = cpuTicket[b]
            cpuTicket[b] = temp

print(cpuTicket)

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
        print("Congratulations! You won on ticket " + str(u + 1) + " with " + str(matches[u]) + " numbers!")
    else:
        print("Sorry. You did not win on ticket " + str(u + 1) + " with only " + str(matches[u]) + " numbers matching.")
    time.sleep(2)

root.mainloop() # Keep window on screen