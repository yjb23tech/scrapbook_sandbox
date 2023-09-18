class NBAPlayer:

    def __init__(self, str_player_name, str_player_position, int_player_attack_power, int_player_defense_power):

        self.str_player_name = str_player_name
        self.str_player_position = str_player_position
        self.int_player_attack_power = int_player_attack_power 
        self.int_player_defense_power = int_player_defense_power 

    def __str__(self):

        return (f"At the {self.str_player_position} position we have: {self.str_player_name}! Attack Power is {self.int_player_attack_power} with a defensive rating of {self.int_player_defense_power}")

#Test to see if the Class works and can be implemented successfully
lebron_james = NBAPlayer("LeBron James", "Small Forward", 100, 99)

print("")
print(lebron_james)
print("")

#All of the above was successful! 


