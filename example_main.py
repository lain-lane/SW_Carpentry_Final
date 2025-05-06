
from Enemies import Snow_Golem, Dragon, Goblin, Snow_Sprite, Magma_Cube
from Player import Player
from Game import Tutorial, Load, Save, Fight

''' This script is a simple example of how the main code is run. The player Joe can be initiated with the Load Function
or by directly defining the hp, max_hp, and xp. The enemy is initiated as one of the imported monsters. Calling Fight
starts the game which can then be saved using the Save function. Calling Tutorial() prints the rules.'''


if __name__=='__main__':

    Protag=Load('save1.rpg')
    # Protag=Player(hp=100,max_hp=100,xp=100)
    Bad_Guy=Magma_Cube
    Fight(Protag,Bad_Guy)
    Save(Protag)

    # Tutorial()