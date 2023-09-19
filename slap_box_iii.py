#The difference between the atk and def should be calculated; result should then be substracted from the hp of the player on defence 
#Can I create a func which actually models the pvp? Would accept objects
#Might consider atk power ups, def boosts, magic and spells...

class Player:

    def __init__(self, str_player_name, str_player_location, int_player_age):
        self.str_player_name = str_player_name
        self.str_player_location = str_player_location 
        self.int_player_age = int_player_age
        self.int_player_atk_power = 1 
        self.int_player_def_power = 1  

    def __str__(self):
        return (f"All the way from {self.str_player_location} we have {self.str_player_name}! He's only {self.int_player_age} years old but be warned, he's deadly in the ring!")

    def int_atk_power(self):
        self.int_player_atk_power = random.randint(1, 20)
        return self.int_player_atk_power 

    def int_def_power(self):
        self.int_player_def_power = random.randint(1, 20)
        return self.int_player_def_power 

#Meta methods 

def str_set_player_name():
    return (input(f"\nWhat is your name Warrior?\n"))

def str_set_player_location():
    return (input(f"\nWhere are you from Warrior?\n"))

def int_set_player_age():
    return (int(input(f"\nAnd how old are you Warrior?\n")))


print("How far can you take it?")
