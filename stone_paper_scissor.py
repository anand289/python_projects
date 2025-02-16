
import random

def result(user_input, response):
    if user_input == response:
        print("Both same, play again")
    elif user_input == 1 and response == 2:
        print("You Lost!")
    elif user_input == 1 and response == 3:
        print("You Won!")
    elif user_input == 2 and response == 1:
        print("You Won!")
    elif user_input == 2 and response == 3:
        print("You Lost!")
    elif user_input == 3 and response == 1:
        print("You Won!")
    elif user_input == 3 and response == 2:
        print("You Won!")
    return

d = {1:"Stone",
     2:"Paper",
     3:"Scissor"}

user_input = int(input("Enter: 1. Stone. 2. Paper 3. Scissor: "))
response = random.randint(1,3)
print("Your Entry: "+ d[user_input])
print("Computer Entry: "+ d[response])
result(user_input,response)


    


