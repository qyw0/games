# -*- coding: utf-8 -*-
"""
Created on Fri Sep  2 16:26:18 2016

@author: qy
"""
import random

fh = open("words.txt", "r")
a = fh.read()
list = a.replace("\n", ",").split(",")
words = []
for i in list:
    words.append(i)
 
def new_game():
    global n, w, a
    n = 6
    w = words[random.randint(1,8)]
    a = ['_', '_', '_', '_']
    d = input("want a new game? [yes/no]  ")
    if d == "yes":
        guess()
    elif d == "no":
        pass

def guess():
    global n
    while n > 0 :
        guess = input("your guess is: ")
        if guess == w[0]:
            a[0] = guess
        if guess == w[1]:
            a[1] = guess
        if guess == w[2]:
            a[2] = guess
        if guess == w[3]:
            a[3] = guess
        n-=1
        print(a)
        if a[0] == w[0] and a[1] == w[1] and a[2] == w[2] and a[3] == w[3]:
            print ("you win")
            new_game()
        if n == 0:
           print ("you lose")
           new_game()
           
new_game()