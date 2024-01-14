import requests
from bs4 import BeautifulSoup


def gaming():

    def wordGenerator(website):
        result = requests.get(website)
        text = result.text
        soup = BeautifulSoup(text, 'lxml')
        wordgen = (soup.find('p', class_='text-center font-18')).find('span').get_text()
        wordgen = wordgen.lower()
        return wordgen

    missCount = 0
    diff = (int(input("Difficulty? 1 - 9")))
    if diff == 1:
        word = wordGenerator("https://www.coolgenerator.com/4-letter-word-generator")
    elif diff == 2:
        word = wordGenerator("https://www.coolgenerator.com/5-letter-word-generator")
    elif diff == 3:
        word = wordGenerator("https://www.coolgenerator.com/6-letter-word-generator")
    elif diff == 4:
        word = wordGenerator("https://www.coolgenerator.com/7-letter-word-generator")
    elif diff == 5:
        word = wordGenerator("https://www.coolgenerator.com/8-letter-word-generator")
    elif diff == 6:
        word = wordGenerator("https://www.coolgenerator.com/9-letter-word-generator")
    elif diff == 7:
        word = wordGenerator("https://www.coolgenerator.com/10-letter-word-generator")
    elif diff == 8:
        word = wordGenerator("https://www.coolgenerator.com/11-letter-word-generator")
    elif diff == 9:
        word = wordGenerator("https://www.coolgenerator.com/12-letter-word-generator")
    else:
        print("Error")

    unknownWord = ("_" * len(word))
    unknownList = list(unknownWord)
    print(unknownList)
    
    while missCount != 3:
        guess = input("Guess a letter")
        to_find = guess
        if len(guess) > 1:
            print("error")
        elif guess not in word:
            missCount = missCount + 1
            print("You got that wrong!")
        else:
            wordindices = ([i for i, x in enumerate(word) if x == to_find])
            for i in range(len(wordindices)):
                unknownList[wordindices[i]] = guess
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
