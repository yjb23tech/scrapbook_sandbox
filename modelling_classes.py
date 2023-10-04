class Tile:

    def __init__(self, int_loc_x, int_loc_y, str_quadrant, str_name):

        self.int_loc_x = int_loc_x
        self.int_loc_y = int_loc_y
        self.str_quadrant = str_quadrant
        self.str_name = str_name 
    
    def __str__(self):
        return (f"{self.str_quadrant} of the map, coordinates {self.int_loc_x}, {self.int_loc_y} on island {self.str_name}")

class Player:

    def __init__(self, str_name, int_loc_x, int_loc_y):

        self.str_name = str_name
        self.int_loc_x = int_loc_x 
        self.int_loc_y = int_loc_y 
    
    def __str__(self):

        print(f"My name is {self.str_name} and and one day I'll be King of the Pirates XD")
    
    