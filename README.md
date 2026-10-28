# Murder at Bennington Manor

A text-based murder mystery game written in Python.

## About This Project

This is an older Python project I created as part of my programming journey. I've preserved the original source code in the `original` folder and included a cleaned, playable version in `src`.

This repository serves as an archive of my original work and something I can continue improving as I develop my programming skills.

## The Mystery

Sir Charles Bennington III has been murdered during a dark and stormy night at Bennington Manor. You play as the detective investigating the crime.

Explore the manor, question the suspects, collect evidence, analyze the clues, and decide who committed the murder. Once you make an accusation, the case is over.

## Features

- Four suspects with different relationships, motives, and alibis
- Six areas of Bennington Manor to investigate
- A murderer selected randomly at the beginning of each game
- Killer-specific evidence
- Generic clues and randomized red herrings
- Suspect interrogation
- Clue collection and review
- Clue analysis hints
- Final accusation and reveal
- Different possible outcomes between playthroughs

## Suspects

- Lilith Bennington — the victim's wife
- Charles Bennington IV — the victim's son
- William Jeeves — the butler
- Joseph Mills — the victim's business partner

## Areas to Investigate

- Dining Room
- Library
- Study
- Kitchen
- Garden
- Bedroom

## Project Structure

```text
murder-at-bennington-manor/
├── original/
│   └── MurderAtBenningtonManor-original.py
├── src/
│   └── MurderAtBenningtonManor.py
├── .gitignore
└── README.md
```

### `original`

Contains the original Python file so the project remains preserved as I originally wrote it.

### `src`

Contains the playable version of the game for continued development.

## How the Game Works

At the beginning of each game, one of the four suspects is randomly selected as the murderer.

As the detective, you can investigate rooms, interrogate suspects, review collected clues, analyze connections, or make an accusation. Rooms contain a mixture of general evidence, red herrings, and clues connected to the murderer selected for that playthrough.

When you are ready, you can accuse a suspect. A correct accusation closes the case; an incorrect accusation allows the real killer to escape.

## Running the Game

Make sure Python 3 is installed on your computer.

From the repository folder, run:

```bash
python src/MurderAtBenningtonManor.py
```

Depending on your system, you may need to use:

```bash
python3 src/MurderAtBenningtonManor.py
```

## Future Improvements

This is a project I can continue expanding as I learn more. Possible improvements include:

- More suspects and rooms
- More varied clues and red herrings
- Stronger connections between evidence and suspect testimony
- Difficulty settings
- A replay option after the final accusation
- Improved clue analysis
- A scoring system for detective performance
- Saving and loading a game
- A graphical interface

## Why Preserve the Original Code?

I wanted to keep the original version rather than simply replace it. The `original` folder provides a snapshot of the project as I originally wrote it, while the `src` folder gives me a place to improve and expand the game over time.
