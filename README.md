# README

### Poblem Statement

 In the game of Ghost, two players take turns building up a word from left to right. Each player contributes one letter per turn. The goal is to not complete the spelling of a word: if you add a letter that completes a word (of 4+ letters), or if you add a letter that produces a string that cannot be extended into a word, you lose. (Bluffing plays and "challenges" may be ignored for the purpose of this puzzle.)

Write a program that plays Ghost optimally against a human, given the following dictionary: WORD.LST. Allow the human to play first. If the computer thinks it will win, it should play randomly among all its winning moves; if the computer thinks it will lose, it should play so as to extend the game as long as possible (choosing randomly among choices that force the maximal game length). A simple console UI will suffice.