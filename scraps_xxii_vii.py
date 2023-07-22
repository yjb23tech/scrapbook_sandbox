#print("\nWarm Ups\n")
#I wanna put the User in a position whereby they end up creating two new arrays: the winner's bracket and the loser's bracket 

def fight(var_hero_marvel_loc, var_hero_dc_loc):

    if (var_hero_marvel_loc > var_hero_dc_loc):
        print("Marvel is the winner!")
    elif (var_hero_marvel_loc == var_hero_dc_loc):
        print("The heroes from both Universes are equally matched: it is a TIE!")
    else:
        print("DC is the winner!")     

arr_heroes_marvel = ['Iron Man', 'Spider Man', 'Mr Fantastic', 'Black Panther', 'Storm'] 
arr_heroes_dc = ['Batman', 'Super Man', 'Cyborg', 'The Flash', 'Wonder Woman'] 

print("\nFrom the Marvel Universe:\n")
for hero_marvel in arr_heroes_marvel:
    print(f"You can choose: {hero_marvel}")

print("\nAnd from the DC Universe:\n")
for hero_dc in arr_heroes_dc:
    print(f"You can choose: {hero_dc}")


ui_hero_marvel_selection = input("\nChoose your Warrior from the Marvel Universe:\n")
ui_hero_dc_selection = input("\nChoose your Warrior from the DC Universe:\n")

print("\nFIGHT\n") 

hero_marvel_loc = (arr_heroes_marvel.index(ui_hero_marvel_selection)) + 1
hero_dc_loc = (arr_heroes_dc.index(ui_hero_dc_selection)) + 1 

fight(hero_marvel_loc, hero_dc_loc)

