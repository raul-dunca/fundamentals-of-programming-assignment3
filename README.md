# Assignment 3

## Requirements
- Use procedural programing and the simple feature-driven software development process
- Provide a command-based console user interface that accepts given commands **exactly** as stated
- Handle the case of incorrect user input by displaying error messages. The program must not crash!
- Use built-in compound types to represent entities in the problem domain and access/modify them using *getter* and *setter* functions
- Have at least 10 items in your application at startup
- Provide **specification** and **tests** for all non-UI functions related to every functionality
- Implement modular programming by having a UI module, a Functions module and a Start module

## Problem Statement

### Contest
  During a programming contest, each contestant had to solve 3 problems (named `P1`, `P2` and `P3`). Afterwards, an evaluation committee graded the solutions to each of the problems using integers between `0` and `10`. The committee needs a program that will allow managing the list of scores and establishing the winners. Write a program that implements the functionalities exemplified below:

**(A) Add the result of a new participant**\
`add <P1 score> <P2 score> <P3 score>`\
`insert <P1 score> <P2 score> <P3 score> at <position>`\
e.g.\
`add 3 8 10` – add a new participant with scores `3`,`8` and `10` (scores for `P1`, `P2`, `P3` respectively)\
`insert 10 10 9 at 5` – insert scores `10`, `10` and `9` at position `5` in the list (positions numbered from `0`)

**(B) Modify scores**\
`remove <position>`\
`remove <start position> to <end position>`\
`replace <old score> <P1 | P2 | P3> with <new score>`\
e.g.\
`remove 1` – set the scores of the participant at position `1` to `0`\
`remove 1 to 3` – set the scores of participants at positions `1`, `2` and `3` to `0`\
`replace 4 P2 with 5` – replace the score obtained by participant `4` at `P2` with `5`

**(C) Display participants whose score has different properties.**\
`list`\
`list sorted`\
`list [ < | = | > ] <score>`\
e.g.\
`list` – display participants and all their scores\
`list < 4` – display participants with an average score `<4`\
`list = 6` – display participants with an average score `=6`\
`list sorted` – display participants sorted in decreasing order of average score
