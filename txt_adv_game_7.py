#print("This script will attempt to re-create the game as so far as the directions in Chp 7")

arr_action_options = ['N to travel North', 'E to travel East', 'S to travel South', 'W to travel West', 'I to access your Inventory', 'Q to save and Quit the game']
arr_inventory_items = ['Dagger', 'Sword', 'Crusty Bread', 'Gold(5)', 'Medical Herbs'] 

def play():

    bool_ui_game_is_on = True
    print("\nEscape from Whole Cake Island XD\n")
    print("Shiver me timbers! It is time to set sail ya swash buckling bilge rats!")

    while (bool_ui_game_is_on):

        print("Make a decision Captain! And be quick about it!\n")

        #Used enumerate() as for loop loop counter variation 
        for x, action in enumerate(arr_action_options, 1):
            print(f"{x}. Press {action}")

        ui_action_test = input("\nWhat is your chosen action Pirate?\n")
        
        #Whole words, letters, symbols 
        if ui_action_test in ['North', 'north', 'N', 'n', '^']:
            print("\nYou're moving North!\n")
        elif ui_action_test in ['East', 'east', 'E', 'e', '>']:
            print("\nYou're moving East!\n")
        elif ui_action_test in ['South', 'south', 'S', 's', 'v']:
            print("\nYou're moving South!\n")
        elif ui_action_test in ['West', 'west', 'W', 'w', '<']:
            print("\nYou're travelling West!\n")
        elif ui_action_test in ['Inventory', 'inventory', 'I', 'i']:
            #Used 'i' as a loop counter outside of the 'for loop' for the variation 
            i = 1
            print(" ")
 
            for item in arr_inventory_items:
                print(f"{i}. {item}")
                i += 1

            print(" ") 
        elif ui_action_test in ['Q', 'q', 'Quit', 'quit']:
            print("\nUntil next time Mugiwara!\n")
            bool_ui_game_is_on = False 
        else:
            print("\nYou have not chosen a valid action; try again!\n")

    print(" ")

play() 
