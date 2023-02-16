#This program demonstrates a guessing game
from random import randint


#get user input
#generate a random number
#check if user number is equal to generated number using a while loop
user_name = input("what is your name")
print("hello there" + user_name + "! " "can you guess the number")
number1 = eval(input("enter number"))
#generate a random number
number = randint(1,50)

counter = 0
while counter < 5:
     user_number = eval(input("enter a number:"))
     counter += 1

     if user_number < random_number:

          print("your guess is too low")

     elif user_number > random_number:

          print("your guess is too high")

     elif user_number == random_number:
          break     
     if user_number == random_number:
          print("you win! ")
     else:
          print("The game is over! The correct number is" ) 
          print(random_number)    


               
