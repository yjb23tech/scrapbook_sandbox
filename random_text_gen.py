#The Black Panther lands a .... on The Amazing Spider Man
#In a shocking turn of events Iron Man has .... the attack from Thor! 

import random

arr_atk_wins_text = ['shattering blow', 'devastating shot to the liver', 'gut wrenching strike to the solar plexus', 'vicious slash', 'critical slam'] 
arr_def_wins_text = ['managed to successfully evade', 'intercepted and then parried', 'deflected and reversed', 'managed to block', 'defend against']

def int_random_dice_roll():
    number = random.randint(0, 4)
    return number

def str_random_txt_gen(pvp_result):

    dice_roll_result = int_random_dice_roll()
    
    if (pvp_result == True):
        atk_wins_txt = arr_atk_wins_text[dice_roll_result]
        return atk_wins_txt
    elif (pvp_result == False):
        def_wins_txt = arr_def_wins_text[dice_roll_result]
        return def_wins_txt
    else:
        draw_wins_txt = "Blah Blah Blah"
        return draw_wins_txt


 

 
