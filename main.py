print("Welcome to my first game!")
name = input("Enter your name: ")
age = input("What is your age? ")

print("Hello", name ,"you are", age, "years old")

'''Checking the player's age'''

if int(age) >= 18:
  print("You are allowed to play the game!")
  
else:
  print("You are not allowed to play the game!")
