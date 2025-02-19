"""
importing the random library and time just for some things
"""
import random
import time
import json

# Carica la configurazione dal file JSON
def load_config(config_file):
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
    Carica la lista di parole da un file.

    Args:
        dirfile (str): Il percorso del file da cui caricare le parole.

    Returns:
        list: Una lista di parole caricate dal file.
    """
    words = []
    try:
        with open(dirfile, 'r', encoding='utf-8') as fil:
            words = fil.read().splitlines()
    except FileNotFoundError:
        print(f"Errore: Il file {dirfile} non è stato trovato.")
    except IOError:
        print(f"Errore: Impossibile leggere il file {dirfile}.")
    return words

def randomword(wordlist):
    """
    Seleziona una parola casuale dalla lista di parole.

    Args:
        wordlist (list): La lista di parole da cui selezionare.

    Returns:
        str: Una parola casuale dalla lista.
    """
    ind = random.randint(0, len(wordlist)-1)
    return wordlist[ind]

def generate(wordlist):
    """
    Genera una lista di parole dove il giocatore deve indovinare quella corretta.

    Args:
        wordlist (list): La lista di parole da cui generare.

    Returns:
        tuple: Una lista di parole generate casualmente e la parola corretta.
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
    Verifica se la parola inserita è corretta.

    Args:
        word (str): La parola inserita dall'utente.
        masterpassword (str): La parola corretta.

    Returns:
        bool: True se la parola è corretta, False altrimenti.
    """
    return word == masterpassword

def letinword(word, masterpassword):
    """
    Conta il numero di lettere corrette nella parola masterpassword dalla parola inserita.

    Args:
        word (str): La parola inserita dall'utente.
        masterpassword (str): La parola corretta.

    Returns:
        str: Il numero di lettere corrette rispetto alla lunghezza della parola corretta.
    """
    nletter = 0
    for letter in word:
        if letter in masterpassword:
            nletter += 1
    return str(nletter) + "/" + str(len(masterpassword))

def main():
    """
    Funzione principale del gioco.
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
