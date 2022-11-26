import random
randdomNumber = random.randint(1,100)
userguess = None
guesses = 0 
print(randdomNumber)
while(userguess!=randdomNumber):
    userguess = int(input("Enter your guess : "))
    guesses += 1
    if(userguess == randdomNumber):
        print("You guessed it right!")
    else:
        if(userguess>randdomNumber):
            print("You guessed it worng! Enter a smaller number")
        else:
            print("You guessed it wrong! enter a larger nubmer")
print(f"You have made {guesses} guesses")

with open("scorelist.txt", "r")as f:
    scorelsit = int(f.read())

if(guesses<scorelsit):
    print("You just broke the previous record")
    with open("scorelist.txt","w") as f:
        f.write(str(guesses))