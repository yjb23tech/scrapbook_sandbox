#print("\nWarm Ups\n")
#I wanna put the User in a position whereby they end up creating two new arrays: the winner's bracket and the loser's bracket 

def fight(var_hero_marvel_loc, var_hero_dc_loc, arr_marvel, arr_dc, arr_cross_winners):

    if (var_hero_marvel_loc > var_hero_dc_loc):
        #print(f"\nAnd your Winner by knockout is {(arr_marvel[var_hero_marvel_loc - 1])}\n")
        #arr_cross_winners.append((arr_marvel[var_hero_marvel_loc - 1]))

        marvel_winner = arr_marvel.pop((var_hero_marvel_loc) - 1)
        print(f"And your Winner by knockout is {marvel_winner}")
        arr_cross_winners.append(marvel_winner)

        dc_loser = arr_dc.pop((var_hero_dc_loc) - 1)
        print(f"And your Loser is {dc_loser}")
 
    elif (var_hero_marvel_loc == var_hero_dc_loc):
        print("The heroes from both Universes are equally matched: it is a TIE!")
    else:
        #print(f"\nIn a shocking upset your Winner is {(arr_dc[var_hero_dc_loc - 1])}\n")
        #arr_cross_winners.append((arr_dc[var_hero_dc_loc - 1]))     

        dc_winner = arr_dc.pop((var_hero_dc_loc) - 1)
        print(f"\nIn a shocking upset your Winner is {dc_winner}")
        arr_cross_winners.append(dc_winner) 

        marvel_loser = arr_marvel.pop((var_hero_marvel_loc) - 1)
        print(f"\nAnd unfortunately your loser is {marvel_loser}")

arr_heroes_marvel = ['Iron Man', 'Spider Man', 'Mr Fantastic', 'Black Panther', 'Storm'] 
arr_heroes_dc = ['Batman', 'Super Man', 'Cyborg', 'The Flash', 'Wonder Woman'] 
arr_heroes_winners = [] 

while (len(arr_heroes_winners) < 5):

    if (len(arr_heroes_marvel) == 1) and (len(arr_heroes_dc) == 1):

        print("Blah Blah Blah")
        arr_heroes_winners.append("Juggernaut")
        continue

    else:

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

        fight(hero_marvel_loc, hero_dc_loc, arr_heroes_marvel, arr_heroes_dc, arr_heroes_winners)


print(f"\nAfter Round 1, your Winners are:\n")

for winner in arr_heroes_winners:
    print(f"Salutations {winner}")


