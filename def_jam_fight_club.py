arr_east_coast_warriors = [] 
arr_west_coast_warriors = [] 

def build_warrior_set(arr_warriors, coast_selection):
    
    while (len(arr_warriors) < 5):
        ui_warrior_creation = input(f"\nName the rapper you'd like to be a Warrior on your {coast_selection} Coast team:\n")
        arr_warriors.append(ui_warrior_creation)

    print(f"\nYour Warrior list for the {coast_selection} team is now complete!")

def print_warrior_set(arr_warriors, coast_selection):
    print(f"\nThese are all of your Warriors for the {coast_selection} Coast team:\n")

    i = 1 
    for warrior in arr_warriors:
        print(f"At position {i}. we have {warrior}")
        i += 1
    print(f"\nThe {coast_selection.upper()} Coast team is ready!\n") 


print("\nWelcome to Def Jam: Fight for Amerikkka!\n")

ui_coast_selection = input("You need to build two teams: one for the East Coast and one for the West Coast. Which team would you like to build first?\n")
print(f"\nYou have chosen to build your {ui_coast_selection.upper()} Coast team first; let's go!")

if ui_coast_selection in ['East', 'east', 'EAST']:
    build_warrior_set(arr_east_coast_warriors, ui_coast_selection)
    print_warrior_set(arr_east_coast_warriors, ui_coast_selection)

else:
    print("You have entered incorrect information; please try again")




