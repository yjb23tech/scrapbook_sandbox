#Desired features
#Dice roll to determine whether Player 1 or Player 2 gets to strike
#Another probability event to determine whether attacking player is successful or not 
#Attack power randomly set to model differences in striking power 

import random 

class Player:
    def __init__(self, str_player_name, str_player_location):
        self.str_player_name = str_player_name
        self.str_player_location = str_player_location
        self.int_player_hp = 100
        self.int_player_atk_power = 1
        self.int_player_def_power = 1 

    def __str__(self):
        return (f"Hailing all the way from {self.str_player_location} please put your hands together and give a warm welcome to {self.str_player_name}!")

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
player_2 = Player(set_player_name(), set_player_location())

print(" ")
print(player_1)
print(player_2)

loop_counter = 1 

while (loop_counter < 6):

    print(f"\nLet round {loop_counter} begin!\n")

    print(f"{player_1.str_player_name} has an attack power of {player_1.int_atk_power()}!")
    print(f"{player_2.str_player_name} has a defensive power of {player_2.int_def_power()}!")

    if (player_1.int_player_atk_power > player_2.int_player_def_power):
        print(f"{player_1.str_player_name} has overwhelmed {player_2.str_player_name} with tremendous force! The damage is severe!")
    elif (player_1.int_player_atk_power < player_2.int_player_def_power):
        print(f"{player_2.str_player_name} is a fortress! {player_1.str_player_name} cannot crack through the impenetrable defense!")
    else:
        print(f"The attacking force of {player_1.str_player_name} and the defensive strength of {player_2.str_player_name} are equally matched! We're in a STALEMATE XD")

    loop_counter += 1 





