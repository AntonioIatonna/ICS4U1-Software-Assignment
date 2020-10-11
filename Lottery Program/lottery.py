from tkinter import *
import time

tickets = []

print("Welcome to Lotto 6/49!\nPlease choose how many tickets you would like to play...")
ticketNumber = int(input())

for x in range(ticketNumber):
    userNumbers = [0, 0, 0, 0, 0, 0]
    print("Please select your numbers for ticket " + str(x + 1))
    for y in range(6):
        print("Please select number " + str(y + 1))
        number = int(input())
        index = 0
        switch = False
        while(switch == False):
            if(number > userNumbers[index]):
                index += 1
            else:
                switch = True
        for i in range(index):
            k = 6 - i
            userNumbers[k + 1] = userNumbers[k]
        userNumbers.insert(index, number)
    tickets.append(userNumbers)
 
print(tickets)