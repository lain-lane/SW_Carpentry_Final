import random

def roll_die(X,advantage=0):
    '''Generates random number to simulate rolling a dice with X sides
    Args:
        advantage=0
            defaults to 0 for no advantage
            +1 for roll with advantage (higher of two rolls)
            -1 for roll with disadvantage (lower of two rolls)'''
    roll_1=random.randint(1,X)
    roll_2=random.randint(1,X)
    if advantage==0:
        return roll_1
    elif advantage<0:
        return min(roll_1,roll_2)
    else:
        return max(roll_1,roll_2)