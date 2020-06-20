answer = 5

print("Please guess a number between 1 and 10: ")
guess = int(input());

#optimized code
if guess == answer:
    print("You've got it first time")
else:
    while guess != answer:
        if guess < answer:
            print("Please guess higher")
        else: # guess is greater than answer
            print("Please guess lower")
        guess = int(input())
        if guess == answer:
            print("Well done, you guessed it")
        else:
            print("Sorry, you are still wrong")


#while guess != answer:
    # if guess < answer:
    #     print ("Please guess higher")
    #     guess = int(input())
    #     if guess == answer:
    #         print("Well done, you guessed it")
    #     else:
    #         print("Sorry you were incorrect")
    # elif guess > answer:
    #     print ("Please guess lower")
    #     guess = int(input())
    #     if guess == answer:
    #         print("Well done, you guessed it")
    #     else:
    #         print("Sorry you were incorrect")
    # else:
    #     print("You got it!")



