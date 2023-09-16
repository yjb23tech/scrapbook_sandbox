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

#A CONSTANT
MAX_WARRIOR_LIST_SIZE = 5 

#AN EMPTY ARR WITH LEN AKA SIZE '0' 
ui_arr_warrior_collection = [] 

#Standard 'while' loop where initial condition checked is the size of the arr; loop will run if size of arr is < 5; size of arr increases each run of loop and size is checked each iteration 
#Use of append function on the arr works to increase the LEN aka SIZE of the arr 
while (len(ui_arr_warrior_collection) < MAX_WARRIOR_LIST_SIZE):
    ui_warrior = input("\nPlease enter the name of your warrior:\n")
    ui_arr_warrior_collection.append(ui_warrior)

print(" ")
for warrior in ui_arr_warrior_collection:
    print(f"Welcome to the battle universe {warrior}")

print(" ")

#FIGHT SCHOOL 

print("Choose your warriors!\n")

ui_warrior_1 = input("Who will your first warrior be?\n")
ui_warrior_2 = input("Who will your second warrior be?\n")

if (arr_marvel_heroes.index(ui_warrior_1) > arr_dc_heroes.index(ui_warrior_2)):
    print(f"In the battle between good and evil we have a winner! The victor is {ui_warrior_1}!")
elif (arr_marvel_heroes.index(ui_warrior_1) < arr_dc_heroes.index(ui_warrior_2)):
    print(f"It cannot be! In the battle between good and evil the villain has come out on top! The victor is {ui_warrior_2}!")
elif (arr_marvel_heroes.index(ui_warrior_1) == arr_dc_heroes.index(ui_warrior_2)):
    print("We have a tie!")
else:
    print("And the winner is... no one?")



