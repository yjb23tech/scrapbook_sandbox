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
print("Logan Roy")    
print("Gus Fring")
print("Peace of Mind")
print("Goya")
print("Paulie Walnuts")
print("K Pop")
print("What To Do?")
print("Grisha")
print("Jack Sparrow")
print("Black Beard")
print("Almost There")
print("Clean Run")
print("Almost Done")
print("Good Day")
print("More")
print("T Minus 1 Year")
print("250_000 GBP Cash")
print("250_000 GBP Cash Cash")
print("The Romantics")
print("Blah Blah Blah")
print("Hilly Committee")
print("Goodfellas Again")
print("Salvage")
print("So fresh and so clean")
print("Back at it")
print("Good Job, Yinka")
print("MJ45")
print("Wake up Neo")
print("I'm under the weather; no work for the past two days")
print("Wayne Wonder")
print("Capo")
print("Soldier")
print("Gunna")
print("Cheating the system")
print("Fake Names")
print("anstrum")
print("I think I'm BIG MEECH!!!")
print("God got Me")
print("Merry Christmas")
print("Investing In My Myself")
print("Let the Benjamins Burn")
print("Goblet of Fire")
print("NBA")
print("New Starts")
print("Whatever come with it")
print("Tanner")
print("Martells of Dawn")
print("Rise!")
print("Faster")
print("For the family")
print("Giannis")
print("Working directly into the Scrimba IDE; Git will starve today but the productivity has been solid, regardless")
