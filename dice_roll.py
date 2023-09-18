import random

def dice_roll():
    number = random.randint(1, 6)
    return number

bool_game_is_on = True

while (bool_game_is_on):

    ui_game_decision = input("\nWould you like to roll the die?\n")
    if (ui_game_decision.upper()) == 'NO':
        print("Thank you for playing; you have now quit the game")
        bool_game_is_on = False

    else:    
        print("Roll the die!\n")
        dice_roll_result = dice_roll()
        print(f"You rolled a {dice_roll_result}")




