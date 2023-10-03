arr_map_grid_tiles_names = ['Island_1', 'Island_2', 'Island_3', 'Island_4', 'Island_5']
arr_user_player_tiles_conquered = ['Island_4', 'Island_3']

arr_tiles_still_to_be_conquered = [] 

for tile in arr_map_grid_tiles_names:

    if tile in arr_user_player_tiles_conquered: #this is the line where things might fail; need to have an adequate response here 
        print(f"Success at {tile}")
    else:
        arr_tiles_still_to_be_conquered.append(tile)

print(" ")
for x, tile in enumerate(arr_tiles_still_to_be_conquered, 1):
    print(f"{x}. {tile} has yet to be conquered!")
print(" ")

#Should have a way of popping each conquered tile such that when you encounter a tile which hasn't been conquered, all tiles from that point on remain 
#can then run a loop to show the tiles outstanding 
#genius 


