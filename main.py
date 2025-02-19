"""
importing the random library and time just for some things
"""
import random
import time
import json


def load_config(config_file):
    """
    Load configuration from a JSON file.

    Args:
        config_file (str): The path to the JSON configuration file.

    Returns:
        dict: The configuration data loaded from the file.
    """
    with open(config_file, 'r', encoding='utf-8') as file:
        return json.load(file)


config = load_config('config.json')

NAME_FILE = config['NAME_FILE']
EFFECT_WAIT_SEC = config['EFFECT_WAIT_SEC']
MAX_NUM_WORD = config['MAX_NUM_WORD']
MIN_NUM_WORD = config['MIN_NUM_WORD']
LENGHT_PER_WORD = config['LENGHT_PER_WORD']
DIFFICULTY = config['DIFFICULTY']


def load_file_word_list(dirfile):
    """
    Load the word list from a file.

    Args:
        dirfile (str): The path to the file from which to load the words.

    Returns:
        list: A list of words loaded from the file.
    """
    words = []
    try:
        with open(dirfile, 'r', encoding='utf-8') as fil:
            words = fil.read().splitlines()
    except FileNotFoundError:
        print(f"Error: The file {dirfile} was not found.")
    except IOError:
        print(f"Error: Unable to read the file {dirfile}.")
    return words


def randomword(wordlist):
    """
    Select a random word from the word list.

    Args:
        wordlist (list): The list of words to select from.

    Returns:
        str: A random word from the list.
    """
    ind = random.randint(0, len(wordlist)-1)
    return wordlist[ind]


def generate(wordlist):
    """
    Generates a list of words where the player
    has to guess the correct one.

    Args:
        wordlist (list): The list of words to generate from.

    Returns:
        tuple: A list of randomly generated words and the correct word
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
    Verifies if the entered word is correct.

    Args:
        word (str): The word entered by the user.
        masterpassword (str): The correct word.

    Returns:
        bool: True if the word is correct, False otherwise.
    """
    return word == masterpassword


def letinword(word, masterpassword):
    """
    Counts the number of correct letters in the masterpassword from the
    entered word.

    Args:
        word (str): The word entered by the user.
        masterpassword (str): The correct word.

    Returns:
        str: The number of correct letters relative to the length of the
        correct word.
    """
    nletter = 0
    for letter in word:
        if letter in masterpassword:
            nletter += 1
    return str(nletter) + "/" + str(len(masterpassword))


def main():
    """
    Main function of the program.
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

    try:
        attempt = int(len(debuglist[0]) / DIFFICULTY)
    except ZeroDivisionError:
        attempt = int(len(debuglist[0]))
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
                # you found the right word
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
