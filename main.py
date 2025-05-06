import random
from Dice import roll_die
from Enemies import Snow_Golem, Dragon
import time
from Player import Player
from Game import Tutorial, Load, Save, Fight

if __name__=='__main__':

    Joe=Load('save1.rpg')
    Joe=Player(100,100,0)
    Evil_Joe=Snow_Golem
    Fight(Joe,Evil_Joe)
    Save(Joe)

    # Tutorial()