print("Welcome to my first game!")
name = input("Enter your name: ")
age = input("What is your age? ")

print("Hello", name ,"you are", age, "years old")

'''Checking the player's age'''

if int(age) >= 18:
  print(f"{name},You are allowed to play the game!Because you are above {age} year old")
  
else:
  print(f"{name},You are not allowed to play the game! Because you are  below {age} year old")
