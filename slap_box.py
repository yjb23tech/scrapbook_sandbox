class Player:

    def __init__(self, str_player_name, str_player_location):
        self.str_player_name = str_player_name
        self.str_player_location = str_player_location
        self.int_player_hp = 100
        self.int_player_atk_power = 20

    def __str__(self):
        return (f"\nPlease welcome to the stage all the way from {self.str_player_location} our latest Warrior {self.str_player_name}\n")

def create_player_name():
    ui_player_name = input("\nWhat is your name Warrior?\n")
    return ui_player_name

def create_player_location():
    ui_player_location = input("\nWhere are you from Warrior?\n")
    return ui_player_location

player_1 = Player(create_player_name(), create_player_location())

print(player_1)

