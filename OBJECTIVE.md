# Project Objective

## Overview

**Fallout Hacking Game** is a command-line word-guessing game that recreates the terminal hacking minigame from the Fallout video game series. The project is a fan-made, pure-Python implementation with no external dependencies.

## Core Goal

Provide a faithful, playable recreation of the Fallout hacking minigame in a terminal environment, where the player must deduce a master password from a set of candidate words within a limited number of attempts.

## Gameplay Objective

1. The game presents the player with a list of 4–10 randomly selected words, all of equal length.
2. One of those words is the hidden master password.
3. The player must guess the correct word within a limited number of attempts (`candidates / DIFFICULTY`).
4. After each wrong guess, the game provides a hint: how many letters from the guess appear anywhere in the master password (e.g., `2/5`).
5. The player wins by guessing the correct word before running out of attempts.

## Design Goals

- **Authenticity**: Mimics the retro terminal aesthetic of Fallout's hacking sequences, including themed output messages and a simulated loading effect.
- **Simplicity**: Pure Python 3, no external dependencies — runs anywhere Python is installed.
- **Configurability**: All game parameters (word list, word length, attempt count, difficulty, visual delay) are controlled via `config.json`.
- **Extensibility**: Supports any language by swapping the word list file (one word per line).
- **Code quality**: PEP 8 compliant, enforced via `flake8` and automated CI/CD checks.

## Technical Scope

| Concern | Approach |
|---|---|
| Language | Python 3.x |
| Word source | Plaintext file (default: Italian, 40k+ words) |
| Word filtering | Words are filtered to an exact configured length |
| Hint system | Letter-overlap count between guess and master password |
| Difficulty | Attempts = `floor(num_candidates / DIFFICULTY)` |
| Configuration | `config.json` — no code changes needed to tune the game |

## Out of Scope

- Graphical or web-based interface
- Networked or multiplayer modes
- Ownership of the Fallout trademark (this is purely a fan project)
