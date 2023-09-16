#print("Thank You For Everything")

arr_marvel_heroes = ['Black Panther', 'Spiderman', 'Iron Man'] 
arr_dc_heroes = ['Super Man', 'Batman', 'Wonder Woman'] 
arr_bleach_heroes = ['Ichigo', 'Kenpachi', 'Yammamato'] 

print(" ")

for hero in arr_marvel_heroes:
    print(f"Welcome to Marvel vs DC {hero}")

print(" ")

for hero in arr_dc_heroes: 
    print(f"Salutations! Welcome to Marvel vs DC {hero}")

print("\nWe have a surprise addition to the combat universe!\n")

for x, hero in enumerate(arr_bleach_heroes, 1):
    print(f"Witness the arrival of {x}. {hero} from the Bleach Universe")

print(" ")

