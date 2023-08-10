#print("Welcome Back")

arr_inventory_items = ['Gold(5)', 'Broad Sword', 'Medicine', 'Iron', 'Potions'] 
arr_action_options = ['N to travel North', 'E to travel East', 'S to travel South', 'W to travel West', 'I to access the items in your Inventory', 'Q to save and Quit the game'] 

def get_user_input():
    return input("\nWhat would you like to do next Captain?\n")

def play():
    bool_game_is_on = True
    print("\nWelcome to Treasure Island! Enter if you dare -_____-\n")

    while (bool_game_is_on):
        for i, action in enumerate(arr_action_options, 1):
            print(f"{i}. Press {action}")

        ui_action = get_user_input()

        if ui_action in ['North', 'NORTH', 'N', 'n', '^']:
            print("\nYou're now travelling North!\n")
        elif ui_action in ['East', 'EAST', 'E', 'e', '>']:
            print("\nYou're now travelling East!\n")
        elif ui_action in ['South', 'SOUTH', 'S', 's', 'v']:
            print("\nYou're now travelling South!\n")
        elif ui_action in ['West', 'WEST', 'W', 'w', '<']:
            print("\nYou're now travelling West!\n")
        else:
            print("\nYou have now saved and quit the game: well done Captain\n")
            bool_game_is_on = False 

play()
