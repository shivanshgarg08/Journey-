# A number guessing game using if/else statements + user input 
import random
x = random.randint(1,20)

user = int(input("Enter Your Guess: " ))

if user == x:
    print("Guess is Correct ")
else:
    print("Guess is wrong ")

if user < x:
    print("Too low")

else:
    print("Too High ")        

# Allowing Multiple Attempts
    