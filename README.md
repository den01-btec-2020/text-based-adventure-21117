# Text-Based Adventure Game

This repository contains the code files for a simple text-based adventure game in Python.

## About this repository

The structure of this repository is as follows:

```
.
+-- README.md
+-- src
|   +-- main.py
|   +-- <other code files>
+-- docs
|   +-- <documentation>
+-- tests
|   +-- <testing documentation>
```

## Installation

There is no explicit installation required. All you need is a way of running Python code. This could be via a [local development environment](https://scott3142.uk/python-programming/codelabs/local-development-environment/) or via some browser-based software such as [Repl.it](https://repl.it/).

## Execution

The game can be played by executing the command `python src/main.py`.

## Requirements

The gameplay should, as closely as possible, satisfy the following requirements:

- Following a welcome message explaining the game, the user enters their name which is then used throughout the program.
- The user starts in a main room with three lives. The theme of the game is up to you to choose.
- The aim of the game is to enter 4 different rooms, collecting items and codes before returning to the main room to complete the game.
- Each room should contain a puzzle which the user has to solve in order to get the item.
-  If the user fails to solve the puzzle after 3 attempts, they lose one life and are ejected from the room.
- If the user loses all of their lives, the game is over and they get the chance to try again.
- If the user collects all of the items and inputs the final correct code before they run out of lives, they win the game.

## Contact

If you have questions about or issues with this repository, please head to the [Github issues](https://github.com/den01-dev/text-based-adventure/issues) board to discuss.
