import random

class Player:

    def __init__(self, str_player_name, str_player_location):
        self.str_player_name = str_player_name
        self.str_player_location = str_player_location
        self.int_player_hp = 100
        self.int_player_atk_power = 20

    def __str__(self):
        return (f"\nPlease welcome to the stage all the way from {self.str_player_location} our latest Warrior {self.str_player_name}!\n")

    def health_status(self):
        print(f"\n{self.str_player_name} has a current health bar of {self.int_player_hp}")

def create_player_name():
    ui_player_name = input("\nWhat is your name Warrior?\n")
    return ui_player_name

def create_player_location():
    ui_player_location = input("\nWhere are you from Warrior?\n")
    return ui_player_location

def dice_roll():
    number = random.randint(1, 6)
    return number

bool_game_is_on = True

player_1 = Player(create_player_name(), create_player_location())
print(player_1)

player_2 = Player(create_player_name(), create_player_location())
print(player_2)

print("Welcome to the Slap Box Fight Club; you're now locked in a death match with no way out until one of you dies XD BEGIN!!!")


while (bool_game_is_on == True):

    ui_keep_playing = input("Would you like to stop playing? Type in Y-E-S to confirm; if you wish to continue type in G-O\n")
    if (ui_keep_playing.upper() == 'YES'):
        print("Thank you for playing; the match is now over!")
        bool_game_is_on = False
    else:
        print("FIGHT ON! ROLL THE DIE REFEREE!")
        dice_roll_result = dice_roll()

        if ((dice_roll_result % 2) == 0):

            print(f"{player_2.str_player_name} has won the dice roll! ATTACK")
            player_1.int_player_hp = player_1.int_player_hp - player_2.int_player_atk_power 
            print(f"After that devastating attack {player_1.str_player_name} is severely injured!")
            player_1.health_status()
            player_2.health_status()

        else:
            print(f"{player_1.str_player_name} has won the dice roll!")
            



        
 
