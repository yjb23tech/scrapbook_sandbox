class NBAPlayer:

    def __init__(self, str_player_name, str_player_position, int_player_attack_power, int_player_defense_power):

        self.str_player_name = str_player_name
        self.str_player_position = str_player_position
        self.int_player_attack_power = int_player_attack_power 
        self.int_player_defense_power = int_player_defense_power 

    def __str__(self):

        return (f"At the {self.str_player_position} position we have: {self.str_player_name}! Attack Power is {self.int_player_attack_power} with a defensive rating of {self.int_player_defense_power}")

#Meta Methods 

def ui_player_name():
    return (input("\nWhat is the name of your player?\n"))

bool_team_builder_is_on = True

#Test to see if the Class works and can be implemented successfully
test_player = NBAPlayer(ui_player_name(), "Small Forward", 100, 99)

print("")
print(test_player)
print("")

#All of the above was successful! 

    
