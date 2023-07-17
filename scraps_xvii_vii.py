print("\nAnd on this rock, I shall build my Church")

#IMMUTABLES 

arr_yard_shop_food_mains = ['curry goat', 'curry chicken', 'oxtail and gravy']
arr_yard_shop_food_sides = ['rice and peas', 'coleslaw', 'dumplings', 'plantins'] 

ui_string_ready_to_order = " "
ui_string_more_to_order = " "  
ui_bool_ready_to_order = False

#FLOW

ui_string_ready_to_order = input("\nY'right darling? Ready to order sum?\n")

#Concatening different case variations of 'Yes' is a waste of time; keeping hear to show my ability to use the 'or' operator but nothing more 
#if (ui_string_ready_to_order == "Yes") or (ui_string_ready_to_order == "yes"):

#A better approach to the above is to have the stored ui var immediately converted into lowercase and then compared against the lower case version of the desired input answer 
#So here we use the .lower() method 
if ((ui_string_ready_to_order.lower()) == "yes"):
    print("Haile Selassie!")
    ui_bool_ready_to_order = True 
else:
    print("Come outta me shop!")
    ui_bool_ready_to_order = False

while (ui_bool_ready_to_order == True):
    
    print("\nFor our mains, we serve:\n")
    for main in arr_yard_shop_food_mains:
        print(main)

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

