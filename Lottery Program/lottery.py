from tkinter import *
import time

tickets = []

print("Welcome to Lotto 6/49!\nPlease choose how many tickets you would like to play...")
ticketNumber = int(input())

tickets = [0] * ticketNumber
for i in range(ticketNumber):
    tickets[i] = [0] * 6

for x in range(ticketNumber):
    print("Please select your numbers for ticket " + str(x + 1))
    for y in range(6):
        print("Please select number " + str(y + 1))
        tickets[x][y] = int(input())

    for j in range(6):
        for k in range(j + 1, 6):
            if(tickets[x][j] > tickets[x][k]):
                temp = tickets[x][j]
                tickets[x][j] = tickets[x][k]
                tickets[x][k] = temp

print(tickets)