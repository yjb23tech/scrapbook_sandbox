#print("Feels good to be back :D")

#WEAPONS CHEST

#PREP OF MY IMMUTABLES 

arr_weapons_chest = ['Rapier', 'Gauntlets', 'Crossbow', 'Broad Sword', 'Spear'] 
var_weapons_chest_counter = 1 

ui_player_name = " " 
ui_weapon_selection = 0  
#ui_player_weapon = " " 

#In the event that the user fails to choose a weapon from the listed options, this boolean counter should be flipped to false 
#The flow of the program should then change accordingly to reflect this decision 
ui_bool_weapon_selection = False

#FLOW

print("\nChoose your weapon Warrior:\n")

while ui_bool_weapon_selection == False:

    var_weapons_chest_counter = 1 

    for weapon in arr_weapons_chest:
        print(f"This is the {weapon}. To use this weapon press {var_weapons_chest_counter}")
        #A really interesting problem has now sprung up as a consequence of using the 'while' loop
        #Because the 'var_weapons_chest_counter' was declared as a global var outside of the loop range, it's assigned value persists causing the values to get progressively higher each time loop runs
        #Two solutions sprint to mind: reset the var each at the beginning of each loop or use a local variable? I wonder which one will work
       
        #Option 1: reset the counter at the start of each loop  
        var_weapons_chest_counter += 1 

    ui_weapon_selection = int(input("\nWhat is your chosen weapon Warrior?\n"))

    #There is a chance that the user may select a number outside of the range described in the menu; the if/else loop works to ensure this is caught and mitigated 
    #We have a clear extreme condition which we want to mitigate - we use the or operator to unify these two extreme; when everything is as normal, the program proceeds uninhibited
    #Beyond and including the two extreme poles we have the range of values we wish to exclude; 'or' operation ensures simultaneous exclusion in both directions
    if (ui_weapon_selection <= 0) or (ui_weapon_selection >= 6):
        print("\nWhere is your weapon Soldier? Do you wish to die? GO AND GET YOUR WEAPON NOW!\n")
        ui_bool_weapon_selection = False

    else:
        #Although the array is 0 indexed, this should be abstracted away from the user which is why the counter begins on 1 
        #But we must return back to the 0 index when accessing values in the array which is why we use the -1; the weapon associated with option '1' is actually indexed at 0 
        #So we subtract 1 to ensure appropriate array index parity between the selection and the actual 0 indexed location of the value within the array
        print(f"\nYou have chosen the {arr_weapons_chest[ui_weapon_selection - 1]}. Are you ready to fight?")

        #Once the weapon selection has been made, it is sensible to store it in a variable so it is readily available elsewhere
        #Unlike loops (I think?) you can actually initialize/instantiate and set a variable locally within the if/else block and then still make use of it outside of the block as normal 
        #Var below doesn't exist until it's created below; but is later still persistent outside of the block  
        ui_player_weapon = arr_weapons_chest[ui_weapon_selection - 1]
        ui_bool_weapon_selection = True


#Outside of the range of the 'while' loop; this block of code should only run once the player has actually chosen and committed to a weapon 
if ui_bool_weapon_selection == False:
    print("\nThis should now actually never be hit as the only way to escape the 'while' loop is if the boolean is changed to True")
else:
    ui_player_name = input("\nI still don't know your name, Warrior: who are you?\n")
    print(f"\nI see. {ui_player_name} of the {ui_player_weapon} - I knew your father: he was a good man.")

print("\nEnd")

