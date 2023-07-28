print("Game On")

arr_inventory = ['Dagger', 'Gold(5)', 'Crusty Bread', 'Iron(3)']
arr_ui_options = ['N for North', 'E for East', 'S for South', 'W for West', 'I for Inventory'] 

def play():

    print("\nWhat you like to do? Choose from the options below:\n")
    i = 1
    for option in arr_ui_options:
        print(f"{i}. Press {option}")
        i += 1
    print(" ")

 
play()
