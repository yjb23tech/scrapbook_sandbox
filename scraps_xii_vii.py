#Warmup exercises conducted on the 12/07/23 
#Use if/elif/else 
#Use a function that accepts parameters 
#Try use a for loop ==> DONE 
#Try use an array ==> DONE
#declare a variable outside of loop; use as a loop counter within for loop ==> DONE
#Declare a variable; use variable as an index which feeds into array; use value returned from indexing array within a print() func statement ==> DONE

#CONSTANTS, FUNCTIONS, IMMUTABLE THINGIES ETC. which will be go on to be used later in the flow declared from here downwards 

arr_sneaker_store = ['Nike Air Force 1', 'Adidas Sambas', 'Reebok Classics']
arr_sneaker_store_tracker = 0 


#FLOW OF PROGRAM BEGINS FROM HERE ONWARDS

print("\nWelcome to ThirdPlaceGoods -_____-\nWe currently have the following sneakers in stock:\n")

for sneaker in arr_sneaker_store:
    print(f"We have lots of the {sneaker}")

print("\nWhich pair of sneakers would you like to purchase? To make a purchase, please follow the instructions below:\n")

for sneaker in arr_sneaker_store:
    print(f"To buy the {sneaker}, please press {arr_sneaker_store_tracker}")
    arr_sneaker_store_tracker += 1 

customer_sneaker_store_order = int(input("\nSo which pair of sneakers would you like? Use the numberpad to choose a pair to buy today XD\n"))
print(f"\nLooks like you're going for the {arr_sneaker_store[customer_sneaker_store_order]} - good choice Sport!")





