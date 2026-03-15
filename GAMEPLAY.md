# Gameplay Documentation

## How to Run

```bash
python3 main.py
```

No external dependencies required. Python 3.x is sufficient.

---

## Game Flow

### 1. Startup Sequence

When launched, the game prints a themed loading sequence that mimics a Fallout
terminal, with a short delay between each line (controlled by `EFFECT_WAIT_SEC`
in `config.json`):

```
Excecuting Debug of the secretCodes.db

initiating preliminary processes
secretCodes.db -> loaded
debug process phase 1/2 -> 'OK'
debug process phase 2/2 -> taking just from 0,122 line
 ...PROCESSING TEXT..
 decrypting MASTER_PASSWORD

Extract from the secretCodes.db
```

### 2. The Word List

After the startup sequence, the game displays all candidate words on one line:

```
jeans ciana lizza vello cesio greve della prude arare
```

- Between **4 and 10** words are shown (configurable via `MIN_NUM_WORD` / `MAX_NUM_WORD`).
- All words have the **same length** (default: 5 characters, set by `LENGHT_PER_WORD`).
- Words are drawn randomly from the word list file (default: Italian).
- One of these words is the hidden **master password**.

### 3. Attempts

The number of attempts is calculated as:

```
attempts = floor(number_of_candidate_words / DIFFICULTY)
```

With the default `DIFFICULTY = 2` and 9 candidate words, the player gets **4 attempts**.

> **Note:** Higher `DIFFICULTY` = fewer attempts = harder game.

---

## Player Interaction

Each round the game prompts:

```
 attempt num > 4
verifyFun() insert string ->
```

The player types one of the displayed words and presses Enter.

### Valid Input

The guess **must** be one of the words shown on screen. Any other input is rejected:

```
INPUT NOT VALID
```

---

## Feedback System

After each **wrong** guess, the game shows how many letters from the guess
appear **anywhere** in the master password:

```
ERROR arare -> 3/5
WRONG WORD attempt num > 3
```

This means: 3 out of 5 letters in `arare` are found somewhere in the master
password. Use this to eliminate or prioritise words.

> **Important:** The hint counts letter *presence*, not *position*.
> A letter is counted once per occurrence in the guess, regardless of where it
> sits in the master password.

### Hint Examples (master password: `jeans`)

| Guess   | Hint | Reasoning |
|---------|------|-----------|
| `arare` | 3/5  | `a`, `r`, `e` appear in `jeans` (a=yes, r=no, a=yes, r=no, e=yes → 3) |
| `della` | 2/5  | `e`, `a` appear in `jeans` |
| `lizza` | 1/5  | only `a` appears in `jeans` |

---

## End States

### Win — Correct Guess

```
ACCESS GRANTED
A WINNAR IS YUO
```

### Lose — Attempts Exhausted

```
COMPUTER LOCKED

NO MORE ATTEMPTS AVAILABLE
```

---

## Full Session Example

Below is a real session trace (9 candidate words, 4 attempts, master = `jeans`):

```
Excecuting Debug of the secretCodes.db

initiating preliminary processes
secretCodes.db -> loaded
debug process phase 1/2 -> 'OK'
debug process phase 2/2 -> taking just from 0,122 line
 ...PROCESSING TEXT..
 decrypting MASTER_PASSWORD

Extract from the secretCodes.db

jeans ciana lizza vello cesio greve della prude arare

 attempt num > 4
verifyFun() insert string -> arare
ERROR arare -> 3/5
WRONG WORD attempt num > 3

 attempt num > 3
verifyFun() insert string -> della
ERROR della -> 2/5
WRONG WORD attempt num > 2

 attempt num > 2
verifyFun() insert string -> lizza
ERROR lizza -> 1/5
WRONG WORD attempt num > 1

 attempt num > 1
verifyFun() insert string -> jeans
ACCESS GRANTED
A WINNAR IS YUO
```

---

## Configuration Quick Reference

All parameters live in `config.json`:

| Key              | Default                  | Effect |
|------------------|--------------------------|--------|
| `NAME_FILE`      | `wordListItaliano.txt`   | Word list source file |
| `EFFECT_WAIT_SEC`| `0.1`                    | Delay (seconds) between startup lines |
| `MAX_NUM_WORD`   | `10`                     | Maximum candidate words shown |
| `MIN_NUM_WORD`   | `4`                      | Minimum candidate words shown |
| `LENGHT_PER_WORD`| `5`                      | Exact length of all words |
| `DIFFICULTY`     | `2`                      | Divides candidate count to set attempts |

---

## Strategy Tips

- Start with words that share **few** letters with each other — this maximises
  the information you gain from the hint.
- A hint of `0/5` is extremely useful: it eliminates every letter in that word
  from consideration.
- A hint equal to the word length (e.g. `5/5`) means all letters of your guess
  are present in the master password, though not necessarily in the same order.
