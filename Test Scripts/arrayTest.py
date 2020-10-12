from tkinter import *
import time

tickets = [0, 0, 0, 0, 0, 0]

for y in range(6):
    print("Please select number " + str(y + 1))
    number = int(input())
    index = 0
    switch = False
    tickets[y] = number
    # while(switch == False):
    #     if(number > userNumbers[index]):
    #         print("if")
    #         index += 1
    #         print("passed")
    #     else:
    #         switch = True
    # for i in range(index):
    #     k = 6 - i
    #     userNumbers[k + 1] = userNumbers[k]
#     userNumbers.insert(index, number)
# tickets.append(userNumbers)
 
print(tickets)