print("\nAnd on this rock, I shall build my Church")

#IMMUTABLES 

arr_yard_shop_food_mains = ['curry goat', 'curry chicken', 'oxtail and gravy', 'jerk chicken', 'achee and saltfish']
arr_yard_shop_food_sides = ['rice and peas', 'coleslaw', 'dumplings', 'plantins'] 

ui_string_ready_to_order = " "
ui_string_more_to_order = " "

ui_int_selected_food_main = 0 
  
ui_bool_ready_to_order = False

#FLOW

ui_string_ready_to_order = input("\nY'right darling? Ready to order sum?\n")

#Concatening different case variations of 'Yes' is a waste of time; keeping hear to show my ability to use the 'or' operator but nothing more 
#if (ui_string_ready_to_order == "Yes") or (ui_string_ready_to_order == "yes"):

#A better approach to the above is to have the stored ui var immediately converted into lowercase and then compared against the lower case version of the desired input answer 
#So here we use the .lower() method 
if ((ui_string_ready_to_order.lower()) == "yes") or ((ui_string_ready_to_order.lower()) == 'y'):
    print("Haile Selassie!")
    ui_bool_ready_to_order = True 
else:
    print("Come outta me shop!")
    ui_bool_ready_to_order = False

while (ui_bool_ready_to_order == True):
    
    local_nested_mains_counter = 1
    print("\nFor our mains, we serve:\n")
    for main in arr_yard_shop_food_mains:
        print(f"To order the {main}, press {local_nested_mains_counter}")
        local_nested_mains_counter += 1

    ui_int_selected_food_main = int(input("\nWhich main would you like? Choose from the options in the menu and use the number pad to submit your choice :D\n"))

    if (ui_int_selected_food_main <= 2) or (ui_int_selected_food_main >= 4):
        print("WE NUH HAVE DAT! ORDER AGAIN AND MEK IT RIGHT\n")
        continue
    else:
        print(f"You've chosen option {ui_int_selected_food_main}")
        print(f"\nThat means your main is the {arr_yard_shop_food_mains[(ui_int_selected_food_main) - 1]}: smart choice XD\n")
    
    print("\nAnd for our sides, we serve:\n")
    for side in arr_yard_shop_food_sides:
        print(side)

    ui_string_more_to_order = input("\nWould you like to order more?\n")

    if (ui_string_more_to_order.lower() == "yes"):
        continue
    else:
        print("It was a pleasure to serve you XD")
        ui_bool_ready_to_order = False

print("\nEnd\n")

