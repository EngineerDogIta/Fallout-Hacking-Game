# Fallout-Hacking-Game

[![No Maintenance Intended](http://unmaintained.tech/badge.svg)](http://unmaintained.tech/)


This is a game made with python that ports the hacking process of the game franchise Fallout

to play the game run the main.py script into the console, the game is currently in italian but to change the language,
you'll need a list of all the words of the language you like.

here is the list of what you can change to make better the game

```
NAME_FILE = 'wordListItaliano.txt'
EFFECT_WAIT_SEC = 0.1
MAX_NUM_WORD = 10
MIN_NUM_WORD = 4
LENGHT_PER_WORD = 5
DIFFICULTY = 2 # NEVER MAKE THIS VALUE 0 I REPEAT NEVER!!!
```

``` NAME_FILE ``` it's the string with the name of the file containing a list of the words to be used in the game, 
``` EFFECT_WAIT_SEC ``` this is the time it takes for each line to be printed into the console, if you want to display every word instantly just make it 0, 
``` MAX_NUM_WORD ``` the game randomly takes a bunch of words this is the maximum it can take, 
``` MIN_NUM_WORD ``` same here the game takes random words from the file with the list of the words, so this is the minimum number of words it takes from it, 
``` LENGHT_PER_WORD ``` this is the lenght for each word that generates, 
``` DIFFICULTY ``` this adjustes the difficulty or the attempts you can do for play, 1 is the easiest one and it's the same number as the number of words generated, 2 takes half of the number of words the game generates and so on

I do not own the Fallout Franchaise trademark, this is just a fan-game that resembles that part of the game, all the code inside are made by "hand".
