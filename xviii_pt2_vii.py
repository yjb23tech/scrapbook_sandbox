print("Game On")

arr_inventory = ['Dagger', 'Gold(5)', 'Crusty Bread', 'Iron(3)']
arr_ui_options = ['N for North', 'E for East', 'S for South', 'W for West', 'I for Inventory', 'Q for Quit'] 

def play():

    print("Escape from Treasure Island")

    ui_bool_game_is_on = True
    
    while (ui_bool_game_is_on):

        print("\nWhat you like to do? Choose from the options below:\n")
        i = 1
        for option in arr_ui_options:
            print(f"{i}. Press {option}")
            i += 1
        print(" ")

        ui_action = input("\nPlease enter your option:\n")
        
        if (ui_action == 'A'):
            print("This has worked")
        elif (ui_action == 'Q'):
            print("You have quit the game now - see you soon!")
            ui_bool_game_is_on = False
        else:
            print("You haven't chosen a valid option; please choose again :D")


play()
