import random
correctNumber = random.randint(1,100)
userNumber = int(input("Enter your number between 1 and 100"))
if userNumber == correctNumber:
    print ("Cool, you guessed the correct number")
elif userNumber >= correctNumber:
    print ("Sorry, your number is to high, would you like to try again? Enter Y/N")
elif userNumber <= correctNumber:
    print ("Sorry, your number is to low")

else:
    print ("I don't understand that guess, please try again")
    