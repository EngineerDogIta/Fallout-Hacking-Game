"""
importing the random library and time just for some things
"""
import random
import time

NAME_FILE = 'wordListItaliano.txt'
EFFECT_WAIT_SEC = 0.1
MAX_NUM_WORD = 10
MIN_NUM_WORD = 4
LENGHT_PER_WORD = 5
DIFFICULTY = 2 # NEVER MAKE THIS VALUE 0 I REPEAT NEVER!!!

def load_file_word_list(dirfile):
    """
    loads from the dirfile file the words
    stores the words in a list and returns it
    """
    words = []
    with open(dirfile, 'r') as fil:
        words = fil.read().splitlines()
    return words

def randomword(wordlist):
    """
    takes a random word from the wordlist
    """
    ind = random.randint(0, len(wordlist)-1)
    return wordlist[ind]

def generate(wordlist):
    """
    generates a list of words where the players has to guess the right one
    """
    debuglist = set()
    max_words = random.randint(MIN_NUM_WORD, MAX_NUM_WORD)
    finito = False
    while not finito:
        word = randomword(wordlist)
        if len(word) == LENGHT_PER_WORD:
            debuglist.add(word)
        if len(debuglist) == max_words:
            finito = True
    newlistwords = list(debuglist)
    return (newlistwords, newlistwords[random.randint(0, len(newlistwords))])

def verifyword(word, masterpassword):
    """
    it checks if it is the right word
    """
    return word == masterpassword

def letinword(word, masterpassword):
    """
    number of correct letters in masterpassword from the word
    """
    nletter = 0
    for letter in word:
        if letter in masterpassword:
            nletter += 1
    return str(nletter) + "/" + str(len(masterpassword))

def main():
    """
    welcome to the easiest hacking tool of the whole time!
    """


    print("Excecuting Debug of the secretCodes.db", "")
    print("")
    print("initiating preliminary processes")

    listwords = load_file_word_list(NAME_FILE)
    time.sleep(EFFECT_WAIT_SEC)
    print("secretCodes.db -> loaded ")

    debuglist = generate(listwords)
    time.sleep(EFFECT_WAIT_SEC)
    print("debug process phase 1/2 -> 'OK' ")

    attempt = int(len(debuglist[0]) / DIFFICULTY)
    time.sleep(EFFECT_WAIT_SEC)
    print("debug process phase 2/2 -> taking just from 0,122 line ")

    listwords = debuglist[0]
    time.sleep(EFFECT_WAIT_SEC)
    print(" ...PROCESSING TEXT.. ")

    masterpass = debuglist[1]
    time.sleep(EFFECT_WAIT_SEC)
    print(" decrypting MASTER_PASSWORD ")
    print("")
    print("Extract from the secretCodes.db")
    print("")
    for word in listwords:
        print(word + " ", end='')
    while attempt != 0:
        print("\n\n attempt num > " + str(attempt))
        inser = str(input("verifyFun() insert string -> "))
        if inser in listwords:
            if verifyword(inser, masterpass):
                # you faound the right words
                print("ACCESS GRANTED")
                break
            else:
                print("ERROR " + str(inser) +
                      ' -> ' + str(letinword(inser, masterpass)))
                print("WRONG WORD attempt num > " + str(attempt-1))
                attempt -= 1
        else:
            print("INPUT NOT VALID")
    if attempt > 0:
        print("A WINNAR IS YUO")
    else:
        print("COMPUTER LOCKED")
        print("")
        print("NO MORE ATTEMPTS AVAILABLE")

if __name__ == '__main__':
    main()
    print('')
    input("Press return to continue ...")
