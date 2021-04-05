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
