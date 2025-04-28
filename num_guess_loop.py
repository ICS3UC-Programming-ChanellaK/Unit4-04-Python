#!/usr/bin/env python3
# Created By: chanella
# Date: April 23, 2025
# The program asks the user to guess a number between 0 and 9
# and then checks if the user guessed correctly and also uses a break statement
# 
import random

def main():
    try:
       # This function uses a break statement
       correct_num = random.randint (0, 9)

       while True:
           # ask the user to guess a number between 0 and 9
           user_num = int(input("Guess a number between 0 and 9:"))
           print("")

           if user_num == correct_num: #check if the user guessed correctly
              print("You guessed correctly!")
              break
           else:
               print("incorrect! try again")
    except ValueError:
      print("Please enter a valid integer between 0 and 9")
        
if __name__ == "__main__":
    main()

        