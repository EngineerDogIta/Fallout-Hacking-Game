# Installation and Running Instructions for the Game

## Prerequisites

Make sure you have Python 3.x installed on your system. You can download and install it from the official [Python](https://www.python.org/) website.

## Installation

1. Clone this repository to your computer:

    ```sh
    git clone https://github.com/EngineerDogIta/Fallout-Hacking-Game.git
    ```

2. Navigate to the project directory:

    ```sh
    cd Fallout-Hacking-Game
    ```

## Configuration

You can customize the game by modifying the following parameters in the config.json file:

```json
{
    "NAME_FILE": "wordListItaliano.txt",
    "EFFECT_WAIT_SEC": 0.1,
    "MAX_NUM_WORD": 10,
    "MIN_NUM_WORD": 4,
    "LENGHT_PER_WORD": 5,
    "DIFFICULTY": 2
}
```

- `NAME_FILE`: Name of the file containing the list of words to be used in the game.
- `EFFECT_WAIT_SEC`: Wait time for printing each line in the console. Set to 0 to display all words immediately.
- `MAX_NUM_WORD`: Maximum number of words the game can randomly pick.
- `MIN_NUM_WORD`: Minimum number of words the game can randomly pick.
- `LENGHT_PER_WORD`: Length of each generated word.
- `DIFFICULTY`: Game difficulty, which determines the number of available attempts. 1 is the easiest and corresponds to the number of generated words, 2 halves the number of attempts, and so on.

## Running the Game

To start the game, run the following command in the console:

```sh
python main.py
```

## Changing Language

To change the language of the game, replace the word list file with another one in the `wordList` directory. The file must contain one word per line.

## Legal Notes

I do not own the trademark of the Fallout series, this is just a fan-game that reproduces that part of the game. All the code inside was written by hand.
