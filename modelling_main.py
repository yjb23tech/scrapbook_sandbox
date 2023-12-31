from modelling_classes import Tile, Player 

arr_world_map = [

    [Tile(0, 0, "South West", "Dressrosa"), Tile(0, 1, "West", "Drum Island"), Tile(0, 2, "North West", "Skypeia")], 
    [Tile(1, 0, "South", "Alabasta"), Tile(1, 1, "Central", "Dawn Island"), Tile(1, 2, "North", "Marineford")], 
    [Tile(2, 0, "South East", "Whole Cake Island"), Tile(2, 1, "East", "Thriller Bark"), Tile(2, 2, "North East", "Wano")]
]

dict_vector_movements_in_y_plane = {

    0: {

        -1: "South", 
        0: "Stay", 
        1: "North"
    }
}

dict_vector_movements_in_x_plane = {

    -1: {

        0: "West"
    },

    0: {

        0: "No Movement"
    }, 

    1: {

        0: "East"
    }


}

user_player = Player("Luffy", 2, 2)

print(" ")
for x in range(len(arr_world_map)):
    for y in range(len(arr_world_map)):
        print(arr_world_map[x][y])
print(" ")

arr_valid_travel_directions = []
arr_invalid_travel_directions = []

#models universal vector movements in the y plane
for x in range(1):
    for y in range(-1, 2):
        #print(f"{x}, {y}")
        #print(f"Can you travel {dict_vector_movements_in_y_plane[x][y]}?")
        try:
            a = user_player.int_loc_x + x 
            b = user_player.int_loc_y + y 

            #print(f"New tile coordinates to be validated: [{a}, {b}]")

            if b < 0:
                raise IndexError 
            
            valid_tile = arr_world_map[a][b]

            #print(f"You can travel {dict_vector_movements_in_y_plane[x][y]} and dock your ship on {valid_tile.str_name}\n")
            str_valid_direction_y = dict_vector_movements_in_y_plane[x][y]
            if str_valid_direction_y == 'Stay':
                continue
            else:
                arr_valid_travel_directions.append(str_valid_direction_y)
        except IndexError:

            #print(f"No you cannot travel {dict_vector_movements_in_y_plane[x][y]}")
            str_invalid_direction_y = dict_vector_movements_in_y_plane[x][y]
            arr_invalid_travel_directions.append(str_invalid_direction_y)


print(" ")
#models universal vector movements in the x plane 
for x in range(-1, 2):
    for y in range(1):
        #print(f"\n{x}, {y}")
        #print(f"Can you travel {dict_vector_movements_in_x_plane[x][y]}?")
        try:
            a = user_player.int_loc_x + x 
            b = user_player.int_loc_y + y 

            #print(f"New tile coordinates to be validated: [{a},{b}]")

            if a < 0:
                raise IndexError
            
            valid_tile = arr_world_map[a][b]

            #print(f"You can travel {dict_vector_movements_in_x_plane[x][y]} and dock your ship on {valid_tile.str_name}\n")
            str_valid_direction_x = dict_vector_movements_in_x_plane[x][y]
            if str_valid_direction_x == 'No Movement':
                continue 
            else:
                arr_valid_travel_directions.append(str_valid_direction_x)
        except IndexError:

            #print(f"No you cannot travel {dict_vector_movements_in_x_plane[x][y]}")
            str_invalid_direction_x = dict_vector_movements_in_x_plane[x][y]
            arr_invalid_travel_directions.append(str_invalid_direction_x)


print(f"Captain {user_player.str_name}! You are currently on {arr_world_map[user_player.int_loc_x][user_player.int_loc_y]} and can travel in the following directions:\n")
i = 1
for valid_direction in arr_valid_travel_directions:
    print(f"{i}. {valid_direction}")
    i += 1 
print(" ")

print("You cannot travel in the following directions:\n")
for z, invalid_direction in enumerate(arr_invalid_travel_directions, 1):
    print(f"{z}. {invalid_direction}")
print(" ")





