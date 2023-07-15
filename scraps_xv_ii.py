#print("Feels good to be back :D")

#WEAPONS CHEST

#PREP OF MY IMMUTABLES 

arr_weapons_chest = ['Rapier', 'Gauntlets', 'Crossbow', 'Broad Sword', 'Spear'] 
var_weapons_chest_counter = 1 

#FLOW

print("\nChoose your weapon Warrior:\n")

for weapon in arr_weapons_chest:
    print(f"This is the {weapon}. To use this weapon press {var_weapons_chest_counter}")
    var_weapons_chest_counter += 1 

ui_weapon_selection = int(input("\nWhat is your chosen weapon Warrior?\n"))

if (ui_weapon_selection <= 0) or (ui_weapon_selection >= 6):
    print("You have failed to choose a weapon; do you wish to die?")
else:
    print(f"\nYou have chosen the {arr_weapons_chest[ui_weapon_selection - 1]}. Are you ready to fight?")

print("\nEnd")

