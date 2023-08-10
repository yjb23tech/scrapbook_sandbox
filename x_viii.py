#print("Welcome Back")

class BroadSword:
    def __init__(self):
        self.name = "Broad Sword"
        self.description = "your strongest and most deadly weapon"
        self.damage = 1_000_000

    #This works; well done
    def __str__(self):
        return (f"This is the {self.name}! It is {self.description} with an attack damage of {self.damage} - weilder beware!")

#This works; well done
arr_inventory_items = ['Gold(5)', BroadSword(), 'Medicine', 'Iron', 'Potions'] 
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

        if ui_action in ['North', 'NORTH', 'north', 'N', 'n', '^']:
            print("\nYou're now travelling North!\n")
        elif ui_action in ['East', 'EAST', 'east', 'E', 'e', '>']:
            print("\nYou're now travelling East!\n")
        elif ui_action in ['South', 'SOUTH', 'south', 'S', 's', 'v']:
            print("\nYou're now travelling South!\n")
        elif ui_action in ['West', 'WEST', 'west', 'W', 'w', '<']:
            print("\nYou're now travelling West!\n")
        elif ui_action in ['Inventory', 'INVENTORY', 'inventory', 'I', 'i']:
            print("\nYou've now accessed the inventory where you have access to the following items:\n")
            for item in arr_inventory_items:
                print(f"{(arr_inventory_items.index(item) + 1)}. {item}")
            print(" ")
        elif ui_action in ['Quit', 'QUIT', 'quit', 'Q', 'q']:
            print("\nYou have now saved and quit the game: well done Captain\n")
            bool_game_is_on = False 
        else:
            print("\nYour input has not been recognised; try again\n")

play()
