from modelling_classes import Tile, Player 

arr_world_map = [

    [Tile(0, 0, "South West", "Dressrosa"), Tile(0, 1, "West", "Drum Island"), Tile(0, 2, "North West", "Skypeia")], 
    [Tile(1, 0, "South", "Alabasta"), Tile(1, 1, "Central", "Dawn Island"), Tile(1, 2, "North", "Marineford")], 
    [Tile(2, 0, "South East", "Whole Cake Island"), Tile(2, 1, "East", "Thriller Bark"), Tile(2, 2, "North East", "Wano")]
]

user_player = Player("Luffy", 1, 1)

print(" ")
for x in range(len(arr_world_map)):
    for y in range(len(arr_world_map)):
        print(arr_world_map[x][y])
print(" ")

print(f"You Captain {user_player.str_name} are currently on {arr_world_map[user_player.int_loc_x][user_player.int_loc_y]}\n")

#models universal vector movements in the y plane
for x in range(1):
    for y in range(-1, 2):
        print(f"{x}, {y}")

#models universal vector movements in the x plane 
for x in range(-1, 2):
    for y in range(1):
        print(f"{x}, {y}")

