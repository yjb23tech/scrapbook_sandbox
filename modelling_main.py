from modelling_classes import Tile

arr_world_map = [

    [Tile(0, 0, "South West", "Dressrosa"), Tile(0, 1, "West", "Drum Island"), Tile(0, 2, "North West", "Skypeia")], 
    [Tile(1, 0, "South", "Alabasta"), Tile(1, 1, "Central", "Dawn Island"), Tile(1, 2, "North", "Marineford")], 
    [Tile(2, 0, "South East", "Whole Cake Island"), Tile(2, 1, "East", "Thriller Bark"), Tile(2, 2, "North East", "Wano")]
]

print(" ")
for x in range(len(arr_world_map)):
    for y in range(len(arr_world_map)):
        print(arr_world_map[x][y])
print(" ")


