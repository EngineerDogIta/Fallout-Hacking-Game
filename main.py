import argparse
import random
import time
import json

# ---------------------------------------------------------------------------
# ANSI color helpers
# ---------------------------------------------------------------------------
GREEN = "\033[32m"
RED = "\033[31m"
YELLOW = "\033[33m"
CYAN = "\033[36m"
RESET = "\033[0m"


def green(s): return f"{GREEN}{s}{RESET}"
def red(s): return f"{RED}{s}{RESET}"
def yellow(s): return f"{YELLOW}{s}{RESET}"
def cyan(s): return f"{CYAN}{s}{RESET}"


# ---------------------------------------------------------------------------
# Config / IO
# ---------------------------------------------------------------------------

def load_config(config_file):
    with open(config_file, 'r', encoding='utf-8') as file:
        return json.load(file)


def load_file_word_list(dirfile):
    words = []
    try:
        with open(dirfile, 'r', encoding='utf-8') as fil:
            words = [line.strip().upper() for line in fil if line.strip()]
    except FileNotFoundError:
        print(red(f"Error: The file {dirfile} was not found."))
    except IOError:
        print(red(f"Error: Unable to read the file {dirfile}."))
    return words


# ---------------------------------------------------------------------------
# Word generation
# ---------------------------------------------------------------------------

def generate(wordlist, config):
    max_words = random.randint(config['MIN_NUM_WORD'], config['MAX_NUM_WORD'])
    valid_words = [w for w in wordlist if len(w) == config['LENGTH_PER_WORD']]

    if not valid_words:
        raise ValueError(
            f"No words found with length {config['LENGTH_PER_WORD']}. "
            "Please check your word list."
        )

    selected = set()
    while len(selected) < max_words and len(selected) < len(valid_words):
        selected.add(random.choice(valid_words))

    newlistwords = list(selected)
    if not newlistwords:
        raise ValueError("Could not generate enough words.")

    return (newlistwords, random.choice(newlistwords))


# ---------------------------------------------------------------------------
# Hint
# ---------------------------------------------------------------------------

def letinword(word, masterpassword):
    """Positional match count: letters correct AND in correct position."""
    nletter = sum(a == b for a, b in zip(word, masterpassword))
    return str(nletter) + "/" + str(len(masterpassword))


# ---------------------------------------------------------------------------
# Display
# ---------------------------------------------------------------------------

FILLER = "......"
HEX_BASE = 0xF4A0
HEX_STRIDE = 12


def display_words(words, removed):
    """
    Show words in a two-column Fallout-style hex-dump layout.
    Removed duds are replaced with filler dots.
    """
    print()
    half = (len(words) + 1) // 2
    left_col = words[:half]
    right_col = words[half:]

    for i, left_word in enumerate(left_col):
        left_addr = cyan(f"0x{HEX_BASE + i * HEX_STRIDE:04X}")
        left_display = FILLER if left_word in removed else left_word

        if i < len(right_col):
            right_word = right_col[i]
            right_addr = cyan(f"0x{HEX_BASE + (half + i) * HEX_STRIDE:04X}")
            right_display = FILLER if right_word in removed else right_word
            left_part = f"  {left_addr}  {left_display:<12}"
            right_part = f"  {right_addr}  {right_display}"
            print(left_part + right_part)
        else:
            print(f"  {left_addr}  {left_display}")
    print()


# ---------------------------------------------------------------------------
# Main game
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(description="Fallout Hacking Minigame")
    parser.add_argument(
        '--config', default='config.json',
        help='Path to the JSON config file (default: config.json)'
    )
    args = parser.parse_args()
    config = load_config(args.config)

    print(cyan("Excecuting Debug of the secretCodes.db"))
    print()
    print("initiating preliminary processes")

    listwords = load_file_word_list(config['NAME_FILE'])
    time.sleep(config['EFFECT_WAIT_SEC'])
    print("secretCodes.db -> loaded ")

    debuglist = generate(listwords, config)
    time.sleep(config['EFFECT_WAIT_SEC'])
    print("debug process phase 1/2 -> 'OK' ")

    try:
        max_attempts = int(len(debuglist[0]) / config['DIFFICULTY'])
    except ZeroDivisionError:
        max_attempts = len(debuglist[0])
    time.sleep(config['EFFECT_WAIT_SEC'])
    print("debug process phase 2/2 -> taking just from 0,122 line ")

    listwords = debuglist[0]
    time.sleep(config['EFFECT_WAIT_SEC'])
    print(" ...PROCESSING TEXT.. ")

    masterpass = debuglist[1]
    time.sleep(config['EFFECT_WAIT_SEC'])
    print(" decrypting MASTER_PASSWORD ")

    attempt = max_attempts
    removed = set()        # duds removed by REMOVE command
    replenish_used = False

    print()
    print(cyan("Extract from the secretCodes.db"))
    display_words(listwords, removed)

    won = False
    while attempt > 0:
        attempt_color = red(str(attempt)) if attempt <= 2 else str(attempt)
        print(f"\n attempt num > {attempt_color}")
        cmd_hint = (
            "  Commands: REMOVE (remove a dud)"
            "  |  REPLENISH (restore attempts, once)"
        )
        print(yellow(cmd_hint))

        try:
            inser = input("  > ").strip().upper()
        except (EOFError, KeyboardInterrupt):
            print("\nAborted.")
            break

        # --- Special commands ---
        if inser == "REMOVE":
            candidates = [
                w for w in listwords if w != masterpass and w not in removed
            ]
            if candidates:
                dud = random.choice(candidates)
                removed.add(dud)
                print(yellow(f"  Dud removed: {dud}"))
                display_words(listwords, removed)
            else:
                print(yellow("  No duds left to remove."))
            continue

        if inser == "REPLENISH":
            if replenish_used:
                print(yellow("  Replenish already used this game."))
            else:
                attempt = max_attempts
                replenish_used = True
                print(yellow(f"  Attempts replenished to {max_attempts}."))
            continue

        # --- Word guess ---
        active_words = [w for w in listwords if w not in removed]
        if inser in active_words:
            if inser == masterpass:
                print(green("ACCESS GRANTED"))
                won = True
                break
            else:
                hint = letinword(inser, masterpass)
                err = red(f"  ERROR {inser}")
                print(err + " -> " + yellow(f"Likeness: {hint}"))
                print(f"  WRONG WORD  attempt num > {attempt - 1}")
                attempt -= 1
        else:
            print(red("  INPUT NOT VALID"))

    if not won:
        print(red("COMPUTER LOCKED"))
        print()
        print(red("NO MORE ATTEMPTS AVAILABLE"))


if __name__ == '__main__':
    main()
    print()
    try:
        input("Press return to continue ...")
    except (EOFError, KeyboardInterrupt):
        pass
