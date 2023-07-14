#Second warm-up for the day; hoping to stretch myself further - need inspiration for more creative activities to do during these freestyle sessions 

#My immutables 

arr_post_office_actions = ['Buy a stamp', 'Sell Euros', 'Ship an item'] 
arr_post_office_actions_counter = 0 

arr_post_office_shipping_cost_light = 1.99
arr_post_office_shipping_cost_medium = 2.99
arr_post_office_shipping_cost_heavy = 3.99 


arr_depop_shippable_goods = ['Sneakers', 'T-Shirt', 'Jeans', 'Jacket', 'Jumper'] 
var_depop_shippable_goods_counter = 0 

def ship_an_item(var_item_weight):
    if (var_item_weight > 0) and (var_item_weight <= 100):
        return arr_post_office_shipping_cost_light 
    elif (var_item_weight > 100) and (var_item_weight < 250):
        return arr_post_office_shipping_cost_medium 
    elif (var_item_weight >= 250) and (var_item_weight < 500):
        return arr_post_office_shipping_cost_heavy
    else:
        print("Your item cannot be shipped")


#FLOW 

ui_ecom_seller_name = input("\nG'day to ya fella! Welcome to the Post Office :D what might your name be?\n")
print(f"\n{ui_ecom_seller_name}! Ayy that's a strong name mate! Well {ui_ecom_seller_name}, what can I do for ya?\n")

for action in arr_post_office_actions: 
    print(f"To {arr_post_office_actions[arr_post_office_actions_counter]} press {arr_post_office_actions_counter}")
    arr_post_office_actions_counter += 1 

ui_ecom_seller_action_num_choice = int(input("\nPlease enter an action using the number pad:\n"))
ui_ecom_seller_action_string_choice = " " 


if (ui_ecom_seller_action_num_choice >= 0) and (ui_ecom_seller_action_num_choice <= 2):
    ui_ecom_seller_action_string_choice = arr_post_office_actions[ui_ecom_seller_action_num_choice] 
    print(f"\nLooks like you've chosen to {ui_ecom_seller_action_string_choice}; how exciting\n")

    if ui_ecom_seller_action_num_choice == 2:
        ui_ecom_seller_item_weight = int(input(f"\nHow much does your item weigh?\n"))
        if (ui_ecom_seller_item_weight > 0) and (ui_ecom_seller_item_weight < 500):
            print(f"\nIt will cost {ship_an_item(ui_ecom_seller_item_weight)} to ship; is that okay?\n")
            print(f"Great! Thank you for your business\n")
        else:
            print("Your item cannot be shipped unfortunately :S")
    else: 
        print("Thank you for your time; see you again soon!")

else: 
    print("This option is invalid") 

print("End...")

print("You always come first")
