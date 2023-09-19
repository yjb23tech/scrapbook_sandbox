#Desired features
#Dice roll to determine whether Player 1 or Player 2 gets to strike
#Another probability event to determine whether attacking player is successful or not 
#Attack power randomly set to model differences in striking power 

import random 

class Player:
    def __init__(self, str_player_name, str_player_location):
        self.str_player_name = str_player_name
        self.str_player_location = str_player_location 

    def __str__(self):
        return (f"Please give a warm welcome to {self.str_player_name} all the way from {self.str_player_location}")

def set_player_name():
    return (input("\nWhat is your name Warrior?\n"))

def set_player_location():
    return (input("\nWhere are you from Warrior?\n"))


print("Welcome to Slap Box ii: Infinity Wars XD")
