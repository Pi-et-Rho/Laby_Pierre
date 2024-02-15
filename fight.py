import random

def dice_throw(min, max):
    return random.randint(min, max)



def calculate_fight():
    TryAgain = True
    result = ""

    while TryAgain:
        TryAgain = False

        party_1 = dice_throw(1, 6)
        party_2 = dice_throw(1, 6)
        
        if party_1 > party_2:
            result = "party_1"
        elif party_1 == party_2:
            TryAgain = True
        elif party_2 > party_1:
            result = "party_2"

        return result