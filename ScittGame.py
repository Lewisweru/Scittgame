import random

correctNumber = random.randrange(1,10)
counter=0
print("Welcome to Lewis' guessing game! Guess a number between 1 and 10. You have 3 trials.")
print("I will give you hints on whether your input is lower than the actual number or greater. Enjoy!")

while(True):
    counter +=1 
    Guessed_number = input("Enter the number you think is correct.")
    if Guessed_number.isdigit():
        Guessed_number=int(Guessed_number)
        if Guessed_number == correctNumber:
          print("Congrats, you got it right!")
          break
        elif Guessed_number < correctNumber and counter != 3:
          print("Too low, try a higher number")
        elif Guessed_number > correctNumber and counter != 3:
          print("Too high, try a lower number")
        if counter == 3:
          print("Oops! You have run out of luck! The correct number was {}".format(correctNumber))
          break
    else:
      print("Invalid input ,please enter a number.")
      counter-=1