import random


def gaming():
    missCount = 0
    diffList = []
    diff = (int(input("Difficulty? 1 - 3")))
    # if diff != (1) or diff != (2) or diff != (3):
    #     print("Error, try again")
    #     gaming()
    if (diff) == 1:
        diffList = ["four", "like", "name", "hand"]
    elif (diff) == 2:
        diffList = ["drive", "knife", "grime", "pants"]
    elif (diff) == 3:
        diffList = ["sevens", "heaven", "wreath", "royals"]
    else:
        print("Error")
    word = diffList[random.randint(0, 3)]
    unknownWord = ("_" * len(word))
    unknownList = list(unknownWord)
    print(unknownList)
    while missCount != 3:
        guess = input("Guess a letter")
        if len(guess) > 1 or guess < "a" or guess > "z":
            print("error")
        elif guess not in word:
            missCount = missCount + 1
            print("You got that wrong!")
        else:
            unknownList[word.index(guess)] = guess
            print(unknownList)
        if "_" not in unknownList:
            missCount = 4
            break
    if missCount == 3:
        print("You ran out of guesses!")
        gameAgain = (input("Do you want to play again? Yes or No"))
        if gameAgain == "Yes" or gameAgain == "yes":
            return gaming()
        else:
            print("Game over")
    if missCount == 4:
        print("You guessed it! The word was '", word, "'!")
        gameAgain = (input("Do you want to play again? Yes or No"))
        if gameAgain == "Yes" or gameAgain == "yes":
            return gaming()
        else:
            print("Game over")

gaming()
