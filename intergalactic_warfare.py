print("\nWelcome to Intergalactic Warfare! Try not to die XD")

arr_heroes = [] 
arr_vilains = [] 

MAX_WARRIOR_LIST_SIZE = 5 

print("It's time to build your combat list!\n")
def ui_build_warrior_list(arr_warriors):

    while (len(arr_warriors) < MAX_WARRIOR_LIST_SIZE):
        ui_warrior_input = input(f"Enter the name of your chosen warrior:\n")
        arr_warriors.append(ui_warrior_input)
        print(" ")


def ui_print_warrior_list(arr_warriors):

    for x, warrior in enumerate(arr_warriors, 1):
        print(f"Please welcome to the stage {x}. {warrior}")

ui_build_warrior_list(arr_heroes)

print("And here are your chosen heroes:\n")

ui_print_warrior_list(arr_heroes)




