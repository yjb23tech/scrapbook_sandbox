print("\nWelcome to Intergalactic Warfare! Try not to die XD")

arr_heroes = [] 
arr_villains = [] 

MAX_WARRIOR_LIST_SIZE = 5 

print("It's time to build your combat list! Choose your heroes:\n")

#This function accepts an empty arr as it's param; using a 'while' loop, loop will run on condition LEN aka SIZE of arr is < 5
#ui input is taken and appended to arr, increasing it in size by +1 each turn
def ui_build_warrior_list(arr_warriors):

    while (len(arr_warriors) < MAX_WARRIOR_LIST_SIZE):
        ui_warrior_input = input(f"Enter the name of your chosen warrior:\n")
        arr_warriors.append(ui_warrior_input)
        print(" ")

#This function accepts an arr; uses a 'for' loop in conjunction with 'enumerate' func to loop through the contents of arr and print item stored in corresponding index location
def ui_print_warrior_list(arr_warriors):

    for x, warrior in enumerate(arr_warriors, 1):
        print(f"Please welcome to the stage {x}. {warrior}")

#Len func on arr returns a integer reflecting size of arr i.e. 5; Range func returns an object which maps to the index locations in the arr using zero indexing so '5' becomes i.e. [0, 1, 2, 3, 4] 
#And so loop will run 5 times; each index location value is mapped to 'x'; needs increment to be intelligible
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



