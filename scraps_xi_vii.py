print("Today is the 11th of July 2023; I'm working in the sandbox")

#Use if/elif/else 
#Use functions 

#Will attempt to model an interaction within a take-out store
#In the event a condition is satisfied total cost of user's order will be calculated and returned for them to pay 

food_option_1_name = "Cheese Burgers"
food_option_1_cost = 4.99
 
food_option_2_name = "Halloumi Fries" 
food_option_2_cost = 2.99

food_option_3_name = "Salmon Sandwiches" 
food_option_3_cost = 5.99

def total_cost(food_option_cost_single, num_of_orders):
    total_order_cost = food_option_cost_single * num_of_orders 
    return total_order_cost 

#I can use 'f' within the input method; surpisingly convenient 
customer_name = input("Welcome to Flappy Burger home of the Flappy Burger - may I take your name?\n")
customer_order_choice = input(f"Great to have you here {customer_name}! What would you like to order?\n")
customer_order_freq = " "

print(f"One sec, I'll see if we have any {customer_order_choice} left for ya!")

if customer_order_choice == food_option_1_name: 
    customer_order_freq = int(input(f"It looks like it might be your lucky day! How many {food_option_1_name} would you like?\n"))
    print(f"That'll be {customer_order_freq} orders of {customer_order_choice} coming right up!")
elif customer_order_choice == food_option_2_name: 
    customer_order_freq = int(input(f"Fresh batch just came out of the kitchen XD! How many orders of {food_option_2_name} would ya like kiddo?\n"))
    print(f"Cor that's a big order hahaha! That'll be {customer_order_freq} orders of {customer_order_choice} Shirley - bag it and tag it for our fav customer")
elif customer_order_choice == food_option_3_name: 
    customer_order_freq = int(input(f"Handmade and ready to go Sailor! How many orders of {food_option_3_name} ya need Captain?\n"))
    print(f"Big baller you are XD! That'll be {customer_order_freq} orders of the {customer_order_choice} for our friend here") 
else: 
    print("Breaks my art to say it but we are all out Sir!")






