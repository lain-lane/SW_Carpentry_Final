import random
from Dice import roll_die
from Enemies import Snow_Golem, Dragon
import time
from Player import Player
from Game import Tutorial, Load, Save, Fight

''' This script is a simple example of how the main code is run. The player Joe can be initiated with the Load Function
or by directly defining the hp, max_hp, and xp. The enemy is initiated as one of the imported monsters. Calling Fight
starts the game which can then be saved using the Save function. Calling Tutorial() prints the rules.'''


if __name__=='__main__':

    # Joe=Load('save1.rpg')
    Joe=Player(hp=100,max_hp=100,xp=100)
    Evil_Joe=Snow_Golem
    Fight(Joe,Evil_Joe)
    Save(Joe)

    # Tutorial()
