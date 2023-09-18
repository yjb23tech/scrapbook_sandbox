#SET UP MY CONSTANTS, FUNCS, ARRs etc. 

arr_nba_east_coast_team = [] 
arr_nba_west_coast_team = [] 
arr_nba_positions = ['Point Guard', 'Shooting Guard', 'Small Forward', 'Power Forward', 'Center'] 

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

build_nba_team(arr_nba_east_coast_team, "East", arr_nba_positions)

#Need a function for printing a team of 5 starting players 

#Need a function to run as the main flow for the program i.e. play() 

#Need a function that evaluates the index locations for a chosen player; compares it against another chosen player; depending on who's higher or lower, loser is popped out of rotation 

 
