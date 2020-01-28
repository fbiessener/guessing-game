"""A number-guessing game."""
from random import randint

# Put your code here
print("Howdy, what's your name?")
name = input("(type in your name) ")
print(f"{name}, I'm thinking of a number between 1 and 100.")
print("Try to guess my number.")
random_num = randint(1, 100)