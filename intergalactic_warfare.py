print("\nWelcome to Intergalactic Warfare! Try not to die XD")

arr_heroes = [] 
arr_villains = [] 

MAX_WARRIOR_LIST_SIZE = 5 

print("It's time to build your combat list! Choose your heroes:\n")

def ui_build_warrior_list(arr_warriors):

    while (len(arr_warriors) < MAX_WARRIOR_LIST_SIZE):
        ui_warrior_input = input(f"Enter the name of your chosen warrior:\n")
        arr_warriors.append(ui_warrior_input)
        print(" ")


def ui_print_warrior_list(arr_warriors):

    for x, warrior in enumerate(arr_warriors, 1):
        print(f"Please welcome to the stage {x}. {warrior}")


def ui_print_warrior_list_alt(arr_warriors):

    for x in range(len(arr_warriors)):
        print(f"Please welcome to the stage {x+1}. {arr_warriors[x]}")


#Build your heroes set
ui_build_warrior_list(arr_heroes)

print("And here are your chosen heroes:\n")

ui_print_warrior_list(arr_heroes)


#Build your villains set 

print("\nIt's time to build your combat list! Choose your villains:\n")

ui_build_warrior_list(arr_villains)

print("And here are your chosen villains:\n")

ui_print_warrior_list_alt(arr_villains)

print("\nLet's fight!\n")



