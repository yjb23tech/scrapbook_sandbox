#Homework piece 0 
def sum_of_squares(int_x, int_y):
    sum_of_squares_result = (int_x * int_x) + (int_y * int_y)
    return sum_of_squares_result 

test_output = sum_of_squares(3, 7) 

print(f"The result of the sum of the squares of 3 and 7 is: {test_output}\n")

#Homework piece 1 

arr_unsorted = [] 
arr_asc_sorted = [] 
loop_max = 3 

while (len(arr_unsorted) < 3):
    user_input = int(input("Enter a number to be sorted:\n"))
    arr_unsorted.append(user_input)

print("\nThe current order of the numbers is:\n")
for x, int in enumerate(arr_unsorted, 1):
    print(f"{x}. {int}")
print(" ")

for x in range(len(arr_unsorted)):

    for y in range(x+1, len(arr_unsorted)):
        if (arr_unsorted[y] < arr_unsorted[x]):
            arr_unsorted[x] = arr_unsorted[y] 
           
print(f"{arr_unsorted}")
    
