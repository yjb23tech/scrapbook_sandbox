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

#There is a chance that the user may select a number outside of the range described in the menu; the if/else loop works to ensure this is caught and mitigated 
#We have a clear extreme condition which we want to mitigate - we use the or operator to unify these two extreme; when everything is as normal, the program proceeds uninhibited
#Beyond and including the two extreme poles we have the range of values we wish to exclude; 'or' operation ensures simultaneous exclusion in both directions
if (ui_weapon_selection <= 0) or (ui_weapon_selection >= 6):
    print("You have failed to choose a weapon; do you wish to die?")
else:
    #Although the array is 0 indexed, this should be abstracted away from the user which is why the counter begins on 1 
    #But we must return back to the 0 index when accessing values in the array which is why we use the -1; the weapon associated with option '1' is actually indexed at 0 
    #So we subtract 1 to ensure appropriate array index parity between the selection and the actual 0 indexed location of the value within the array
    print(f"\nYou have chosen the {arr_weapons_chest[ui_weapon_selection - 1]}. Are you ready to fight?")
    #Once the weapon selection has been made, it is sensible to store it in a variable so it is readily available elsewhere 
    ui_player_weapon = arr_weapons_chest[ui_weapon_selection - 1]

ui_player_name = input("\nI still don't know your name, Warrior: who are you?\n")

print(f"\nI see. {ui_player_name} of the {ui_player_weapon} - I knew your father: he was a good man.")

print("\nEnd")

