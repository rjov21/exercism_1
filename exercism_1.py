# -*- coding: utf-8 -*-
"""
Created on Mon Apr  5 17:11:40 2021

@author: DIOS BENDITO
"""

# Reverse string


def reverse(text="Ramen"):
    a = ""
    for i in text:
        a = i + a
    return a


# high scores


def latest(scores=[100, 0, 90, 30]):
    expected = int(scores[len(scores) - 1])
    return expected


def personal_best(scores=[100, 0, 90, 30]):
    scores.sort()
    x = scores[(len(scores) - 1):]
    mayor = x[0]
    return mayor


def personal_top_three(scores=[100, 0, 90, 30]):
    scores.sort()
    if len(scores) < 3:
        x = scores[:]
    else:
        x = scores[(len(scores) - 3):]
    mayor = []
    for i in range(0, len(x)):
        mayor.append(x[len(x) - i - 1])
    return mayor


# scrabble score
def score(word=""):
    scorefinal = 0
    for i in word:
        if i == "a" or i == "e" or i == "i" or i == "o" or i == "u" or i == "l" or i == "n" or i == "r" or i == "t" or i == "s":
            scorefinal = scorefinal + 1
        if i == "d" or i == "g":
            scorefinal = 2 + scorefinal
        if i == "b" or i == "c" or i == "m" or i == "p":
            scorefinal = scorefinal + 3
        if i == "f" or i == "v" or i == "h" or i == "w" or i == "y":
            scorefinal = scorefinal + 4
        if i == "k":
            scorefinal = scorefinal + 5
        if i == "j" or i == "x":
            scorefinal = scorefinal + 8
        if i == "q" or i == "z":
            scorefinal = scorefinal + 10
        if i == "A" or i == "E" or i == "I" or i == "O" or i == "U" or i == "L" or i == "N" or i == "R" or i == "T" or i == "S":
            scorefinal = scorefinal + 1
        if i == "D" or i == "G":
            scorefinal = 2 + scorefinal
        if i == "B" or i == "C" or i == "M" or i == "P":
            scorefinal = scorefinal + 3
        if i == "F" or i == "V" or i == "H" or i == "W" or i == "Y":
            scorefinal = scorefinal + 4
        if i == "K":
            scorefinal = scorefinal + 5
        if i == "J" or i == "X":
            scorefinal = scorefinal + 8
        if i == "Q" or i == "Z":
            scorefinal = scorefinal + 10
    return scorefinal


# acronym
def abbreviate(words):
    a = ""
    z = 0
    a = a + words[0]
    for i in words:
        if i == " " or i == "-" or i == "_":
            r = words[z + 1]
            if r == "-" or r == "_" or r == " ":
                s = words[z + 2]
                a = a + s
            else:
                a = a + r
        z += 1
    return a.upper()


# hey bob
def response(hey_bob):
    answer = ""
    if hey_bob[len(hey_bob) - 1] == "?":
        answer = "sure."
    if hey_bob == hey_bob.upper():
        answer = "Whoa, chill out!"
    if hey_bob[0] == "¿" and hey_bob[len(hey_bob) - 1] == "?":
        answer = "Calm down, I know what I'm doing!"
    if hey_bob == "":
        answer = "Fine. Be that way!"
    else:
        answer = "Whatever."
    return answer
