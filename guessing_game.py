"""
Created on Thu Mar  9 07:05:21 2023

@author: ghild
"""

#GUESSING GAME 
import random

chance= 5
print("you will be given "+str( chance ) +" chances")
for i in range(chance):
    comp_num=random.randrange(1,399)
    user_num=int(input("Enter number "))
    if(comp_num<user_num):
        print("random number is",comp_num)
        print("your guess is too high")
    elif(comp_num>user_num):
        print("random number is",comp_num)
        print("your guess is too low")
    else:
        print("random number is",comp_num)
        print("correct")
