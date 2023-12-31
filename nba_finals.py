#SET UP MY CONSTANTS, FUNCS, ARRs etc. 

arr_nba_east_coast_team = [] 
arr_nba_west_coast_team = [] 
arr_nba_positions = ['Point Guard', 'Shooting Guard', 'Small Forward', 'Power Forward', 'Center'] 

bool_game_is_on = True

#Need a function for building a team of 5 starting players

def build_nba_team(arr_nba_team, coast_selection, arr_positions):
    print(f"\nYou have chosen to build your {coast_selection} Coast team; let's get started XD")

    x = 0 
    while(len(arr_nba_team) < 5):
        ui_nba_player = input(f"\nWhich player would you like to have in your {coast_selection.upper()} Coast team at the {arr_nba_positions[x]} position?\n")
        arr_nba_team.append(ui_nba_player)
        x += 1 
 
    print("\nYour team is complete; here is your team:\n")
    i = 1 
    for warrior in arr_nba_team:
        print(f"At position {i}. we have: {warrior}\n")
        i += 1 

    print(f"Let's goooooo {coast_selection.upper()} Coast team!\n")

def play():

    print("\nWelcome to the NBA finals! Which team would you like to build first? East or West?\n")
    ui_coast_selection = input("To build the East Coast team, type in E-A-S-T or to build the West Coast team type in W-E-S-T:\n")

    if (ui_coast_selection.upper()) == 'EAST':

        print(f"You have chosen to build the East Coast team; let's go!")
        build_nba_team(arr_nba_east_coast_team, ui_coast_selection, arr_nba_positions)

        print("\nAnd now you must build the West Coast team; let's go!\n")
        build_nba_team(arr_nba_west_coast_team, "West", arr_nba_positions)

    elif (ui_coast_selection.upper()) == 'WEST':

        print(f"You have chosen to build the {ui_coast_selection.upper} Coast team; let's go!")
        build_nba_team(arr_nba_west_coast_team, ui_coast_selection, arr_nba_positions)

        print("\nAnd now you must build the East Coast team; let's go!\n")
        build_nba_team(arr_nba_east_coast_team, "East", arr_nba_positions)

    else:
        print("Invalid selection; try again!")

    
    print(arr_nba_east_coast_team)
    print(arr_nba_west_coast_team)
    print(" ")

    while ((len(arr_nba_east_coast_team) > 0) and (len(arr_nba_west_coast_team) > 0)):

        print(arr_nba_east_coast_team)
        print(arr_nba_west_coast_team)
        print(" ")

        ui_nba_east_coast_player = input("\nChoose a player from your East Coast team:\n")
        ui_nba_west_coast_player = input("\nChoose a player from your West Coast team:\n")

        ui_nba_east_coast_player_rank = arr_nba_east_coast_team.index(ui_nba_east_coast_player)
        ui_nba_west_coast_player_rank = arr_nba_west_coast_team.index(ui_nba_west_coast_player)

        if (ui_nba_east_coast_player_rank > ui_nba_west_coast_player_rank):
            print(f"{ui_nba_east_coast_player} went head to head with {ui_nba_west_coast_player} and dunked all over him!")
            ui_nba_west_coast_player_removal = arr_nba_west_coast_team.pop(ui_nba_west_coast_player_rank)
            print(f"{ui_nba_west_coast_player_removal} is out XD")

        elif (ui_nba_east_coast_player_rank < ui_nba_west_coast_player_rank):
            print(f"{ui_nba_west_coast_player} absolutely posterized {ui_nba_east_coast_player} with no regard for human LIFE")
            ui_nba_east_coast_player_removal = arr_nba_east_coast_team.pop(ui_nba_east_coast_player_rank)
            print(f"{ui_nba_east_coast_player_removal} is out XD")

        elif (ui_nba_east_coast_player_rank == ui_nba_west_coast_player_rank):
            print("Players are tied! Try again XD")

        else:
            print("Invalid input; try again")



play()

#Need a function to run as the main flow for the program i.e. play() 

#Need a function that evaluates the index locations for a chosen player; compares it against another chosen player; depending on who's higher or lower, loser is popped out of rotation 

 
