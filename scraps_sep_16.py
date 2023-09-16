#print("Thank You For Everything")

arr_marvel_heroes = ['Black Panther', 'Spiderman', 'Iron Man'] 
arr_dc_heroes = ['Super Man', 'Batman', 'Wonder Woman'] 
arr_bleach_heroes = ['Ichigo', 'Kenpachi', 'Yammamato'] 

print(" ")

#Standard for loop where we loop through an array
for hero in arr_marvel_heroes:
    print(f"Welcome to Marvel vs DC {hero}")

print(" ")

#Standard for loop where we loop through an array
for hero in arr_dc_heroes: 
    print(f"Salutations! Welcome to Marvel vs DC {hero}")

print("\nWe have a surprise addition to the combat universe!\n")

#Standard for loop in conjunction with the enumerate function; remember, it works back to front
for x, hero in enumerate(arr_bleach_heroes, 1):
    print(f"Witness the arrival of {x}. {hero} from the Bleach Universe")

print(" ")

warrior_counter = 1 
arr_naruto_heroes = ['Haku', 'Zabuza', 'Raikage', 'Yondaime'] 

#Standard for loop in conjunction with a counter that is incremented following each loop through; counter must be declared outside of the for loop otherwise it will reset 
for hero in arr_naruto_heroes:
    print(f"And next to the stage we have {warrior_counter}. {hero}")
    warrior_counter += 1 

print(" ")

#Build your own warrior list 

MAX_WARRIOR_LIST_SIZE = 5 

ui_arr_warrior_collection = [] 

while (len(ui_arr_warrior_collection) < MAX_WARRIOR_LIST_SIZE):
    ui_warrior = input("\nPlease enter the name of your warrior:\n")
    ui_arr_warrior_collection.append(ui_warrior)

print(" ")
for warrior in ui_arr_warrior_collection:
    print(f"Welcome to the battle universe {warrior}")

print(" ")


