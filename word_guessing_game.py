# -*- coding: utf-8 -*-
"""
Created on Sat Dec 28 15:21:03 2024

@author: SambesiweSli
"""

import random

print("Hi, welcome to another guessing game.\nIn this game we have to guess a word. \nYou only have a limited number of tries.So best of luck to you.\nLET'S GET STARTED!!")

name = input("What is your name?\n")

print("Good Luck!", name)

#list of words that the user will need to guess from.
list_of_words = ['Computers', 'Programming', 'Python', 'Mathematics', 'Sofware Engineering',
                 'Mathematics', 'Django', 'Backend', 'Frontend', 
                 'FullStack', 'Spyder', 'Jupyter', 'PyCharm']

#this is where a random word from the list is generated.
word = random.choice(list_of_words)

print("Okay, let's start guessing.")

#Initializing guesses and attempts at guessing a character
guesses = " "
attempts = 12

#this is where the loop of the game starts
#main section of the code
while attempts > 0:
    
    #this is where we check each character of the word
    failed = 0
    for character in word:
        
        if character in guesses:
            print(character, end=" ")
        else:
            print("_")
            failed += 1
    #checking to see if the user has won or not            
    if failed == 0:
        print("\n")
        print("\nWELL DONE!! You Win")
        print("The word is:", word)
        break
    
    print()
    guess = input("guess a character: ")
    guesses += guess

    #this section handles the incorrect guesses
    if guess not in word:
        attempts -= 1
        print("WRONG!! try again")
        print("You have", + attempts, "more guesses left")
    
    #here we check to see if the user has lost or not.
    if attempts == 0:
        print("YOU LOSE!! better luck next time.")