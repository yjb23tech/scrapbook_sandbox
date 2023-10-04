arr_island_list_complete = ['Island_1', 'Island_2', 'Island_3', 'Island_4', 'Island_5', 'Island_6', 'Island_7', 'Island_8', 'Island_9']
arr_island_list_conquered = ['Island_1', 'Island_9', 'Island_7', 'Island_4', 'Island_2', 'Island_3', 'Island_5', 'Island_6']
arr_island_list_unconquered = []

print("\nLet's review:\n")
for island in arr_island_list_complete:
    if island in arr_island_list_conquered:
        print(f"You have successfully conquered {island}")
    else:
        arr_island_list_unconquered.append(island)

print("\nIn summary:\n")
if (len(arr_island_list_unconquered) == 0):
    print("Congratulations - you have defeated the game Sailor\n")
else:
    x = 1
    for island in arr_island_list_unconquered:
        print(f"You are still yet to conquer: {x}. {island}")
        x += 1 
    print(" ")

