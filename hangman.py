import requests
from bs4 import BeautifulSoup


CHAR_MIN = 4
CHAR_MAX = 7
MISSCOUNT_MAX = 7


def gaming():

    def wordGenerator(website):
        result = requests.get(website)
        text = result.text
        soup = BeautifulSoup(text, 'lxml')
        wordgen = (soup.find('p', class_='text-center font-18')).find('span').get_text()
        wordgen = wordgen.lower()
        return wordgen

    def checkLetter(word, guess):
        wordindices = ([i for i, x in enumerate(word) if x == guess])
        for i in range(len(wordindices)):
            unknownList[wordindices[i]] = guess
        print(unknownList)


    diff = 0
    while diff < CHAR_MIN or diff > CHAR_MAX:
        diff = input("Length of word? " + str(CHAR_MIN) + " - " + str(CHAR_MAX) + "  ")
        flag = True
        try:
            diff = int(diff)
        except ValueError:
            flag = False
            diff = 0
            print("Error. Type an integer only.")

        if flag:
            if diff >= CHAR_MIN and diff <= CHAR_MAX:
                string = "https://www.coolgenerator.com/"+str(diff)+"-letter-word-generator"
                word = wordGenerator(string)
            else:
                print("Error. Type a number within", CHAR_MIN, "-", CHAR_MAX,".")

    # generates blank word
    unknownWord = ("_" * len(word))
    unknownList = list(unknownWord)
    print(unknownList)

    missCount = 0
    while missCount != MISSCOUNT_MAX:
        guess = input("Guess a letter")
        if len(guess) > 1:
            print("error")
        elif guess not in word:
            missCount = missCount + 1
            print("You got that wrong! You have", MISSCOUNT_MAX-missCount, "guesses left!")
        else:
            checkLetter(word, guess)
        if "_" not in unknownList:
            missCount = MISSCOUNT_MAX + 1
            break
    return missCount, word


missCount = 0
print("Hangman starts!")
while missCount <= MISSCOUNT_MAX:
    missCount, word = gaming()

    if missCount == MISSCOUNT_MAX:
        print("You ran out of guesses!")
    else:
        print("You guessed it! The word was '", word, "'!")

    gameAgain = (input("Do you want to play again? Yes or No"))
    if gameAgain == "N" or gameAgain == "n":
        print("Game over")
        exit(0)
    if gameAgain == "Y" or gameAgain == "y":
        missCount = 0
    else:
        print("Error. Game over")
        exit(1)
