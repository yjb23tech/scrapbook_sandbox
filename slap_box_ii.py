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
        return (f"\nPlease give a warm welcome to {self.str_player_name} all the way from {self.str_player_location}\n")

    def int_atk_power(self):
        self.int_player_atk_power = random.randint(1, 20)
        return self.int_player_atk_power

    def int_def_power(self):
        self.int_player_def_power = random.randint(1, 20)
        return self.int_player_def_power 

def set_player_name():
    return (input("\nWhat is your name Warrior?\n"))

def set_player_location():
    return (input("\nWhere are you from Warrior?\n"))


print("\nWelcome to Slap Box ii: Infinity Wars XD")

player_1 = Player(set_player_name(), set_player_location())

print(player_1)

loop_counter = 0 

while (loop_counter < 5):
    print(f"{player_1.str_player_name} has an attack power of {player_1.int_atk_power()}")
    print(f"{player_1.str_player_name} has a defensive power of {player_1.int_def_power()}\n")

    loop_counter += 1 





