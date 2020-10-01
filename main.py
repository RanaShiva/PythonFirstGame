print("Welcome to my first game!")
name = input("Enter your name: ")
age = input("What is your age? ")

print("Hello", name ,"you are", age, "years old")

'''Checking the player's age'''

if int(age) >= 18:
  print("You are allowed to play the game!")
  
else:
  print("You are not allowed to play the game!")
print("so the game is ... choose a number from 1 to 5 i will tell your luck")
num = int(input())
if(num == 1):
  print("You are the luckiest man in the world")
elif(num == 2):
  print("You are the strongest person")   
elif(num == 3):
  print("You wil marry in a royal family")
elif(num == 4):
  print("you are physically weak, work hard")
elif(num == 5):
  print("your luck is not good, go to priest!!)
else:
  print("very clever to choose it")
  print("You are the most wanted person")
