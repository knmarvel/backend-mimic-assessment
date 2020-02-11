#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/
# Kano's notes: I spent 2 hrs on with this assignment.

"""Mimic pyquick exercise -- optional extra exercise.
Google's Python Class

Read in the file specified on the command line.
Do a simple split() on whitespace to obtain all the words in the file.
Rather than read the file line by line, it's easier to read
it into one giant string and split it once.

Build a "mimic" dict that maps each word that appears in the file
to a list of all the words that immediately follow that word in the file.
The list of words can be be in any order and should include
duplicates. So for example the key "and" might have the list
["then", "best", "then", "after", ...] listing
all the words which came after "and" in the text.
We'll say that the empty string is what comes before
the first word in the file.

With the mimic dict, it's fairly easy to emit random
text that mimics the original. Print a word, then look
up what words might come next and pick one at random as
the next word.
Use the empty string as the first word to prime things.
If we ever get stuck with a word that is not in the dict,
go back to the empty string to keep things moving.

Note: the standard python module 'random' includes a
random.choice(list) method which picks a random element
from a non-empty list.

For fun, feed your program to itself as input.
Could work on getting it to put in linebreaks around 70
columns, so the output looks better.

"""

import random
import sys


__author__ = "github.com/knmarvel"


def create_mimic_dict(filename):
    """Returns mimic dict mapping each word to list of words which follow it. 
    For example:
        Input: "I am a software developer, and I don't care who knows"
        Output: 
            {
                "" : ["I"],
                "I" : ["am", "don't"], 
                "am": ["a"], 
                "a": ["software"],
                "software" : ["developer,"],
                "developer," : ["and"],
                "and" : ["I"],
                "I" : ["don't"],
                "don't" : ["care"],
                "care" : ["who"],
                "who" : ["knows"]
            }
    """
    mimic_dict = {}
    with open(filename, "r") as words:
        words = words.read()
    words = words.replace("\n", " ")
    words_list = [x for x in words.split(" ")]
    for x in words_list:
        mimic_dict[x] = []
    mimic_dict.pop(words_list[-1])
    for x in mimic_dict:
        if x == "":
            mimic_dict[x] = words_list[0]
        for y in range(len(words_list)):
            if words_list[y] == x:
                mimic_dict[x] = list(mimic_dict[x])
                mimic_dict[x].append(words_list[y + 1])
    mimic_dict[""] = words_list[0]
    return(mimic_dict)


def print_mimic(mimic_dict, start_word):
    """Given a previously compiled mimic_dict and start_word, prints 200 random words:
        - Print the start_word
        - Lookup the start_word in your mimic_dict and get it's next-list
        - Randomly select a new word from the next-list
        - Repeat this process 200 times
    """
    new_thoughts = [mimic_dict[start_word]]
    start_word = mimic_dict[start_word]
    for x in range(200):
        if start_word in list(mimic_dict.keys()):
            start_word = random.choice(mimic_dict[start_word])
        else:
            start_word = mimic_dict[""]
        if start_word == "I" or start_word == "O" or start_word == "a" or len(start_word) > 1:
            new_thoughts.append(start_word)
    print(" ".join(new_thoughts))


# # Provided main(), calls mimic_dict() and mimic()
def main():
    print(sys.argv)
    if len(sys.argv) != 2:
        print ('usage: python mimic.py file-to-read')
        sys.exit(1)

    d = create_mimic_dict(sys.argv[1])
    print_mimic(d, '')


if __name__ == '__main__':
    main()
