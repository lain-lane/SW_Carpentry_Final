import random
from Dice import roll_die
from Enemies import Snow_Golem, Dragon
import time
from Player import Player

    
def Fight(player, enemy):
    '''starts a fight that runs until someone dies or player quits
    ***Args***
        player: Player object
        enemy: Enemy object''' 
        
    quitter=False # this flag closes the loop if the player quits
    turn_counter=1 # player goes first (positive), enemy's turn will be negative

    actions_dict=player.actions_dict 
    
    # continues until someone quits or dies
    while player.hp>0 and enemy.hp>0 and quitter==False:
        # ENEMY TURN
        if turn_counter<0:
            time.sleep(0.8) # delaying print to make it easier to read
            print(enemy.name+' HP: '+ str(enemy.hp))
            damage=enemy.attack(player) # call on the enemy's attack function
            print(enemy.name+' dealt ' + str(damage)+ ' dmg')
            turn_counter=-turn_counter

        # PLAYER TURN
        else:
            print('Your HP: '+ str(player.hp))
            action=player.actions_input() # calls on a function that validates input

            if action in actions_dict:
                spell=actions_dict[action] # grab corresponding spell from the dictionary 
                if spell.aspect=='heal': # so that the heal helps yourself
                    spell.cast(player)
                else:
                    spell.cast(enemy)
            elif action=='quit': # quits loop
                quitter=True
            turn_counter=-turn_counter
        print('-'*100)
            

    if enemy.hp<=0:
        enemy.die(player) # this function adds the xp to the player
        print('Enemy died and dropped '+str(enemy.drop)+ ' xp')
    elif player.hp<=0:
        print('You died! Game over.')



def Tutorial():
    '''prints some basic instructions about the game
    ***Args: none
    ***Returns: none'''
    
    print('-'*100+'\n')
    print('Welcome to the Command Line Interface Fantasy Role Playing Game (CLIF RPG)\n')
    print('You are a young wizard. Fight enemies to gain XP and learn new spells.\n')
    print('During a fight, type the number that corresponds to the spell you want to cast.')
    print('To read what a spell does, type "inspect X" where X is the number of the spell.\n')
    print('To end a fight early, type "quit".\n')
    print('Have fun!\n')
    print('-'*100+'\n')

def Save(player,filename='save1.rpg'):
    '''saves player stats to .rpg file
    ***Args***
        player: Player
            instance of the Player object
        filename: str
            name to save to, defaults to save1
    *** Returns ***
        none'''
    # grabs stats from the player input
    hp=player.hp
    max_hp=player.max_hp
    xp=player.xp
    # writes each stat with the first letter as a key
    f=open(filename,'w')
    f.write('H '+str(hp)+'\n')
    f.write('M '+str(max_hp)+'\n')
    f.write('X '+str(xp))
    f.close()
    return

def Load(filename='save1.rpg'):
    '''loads information from the .rpg file format
    ***Args***
        filename: str
            name of file to read, defaults to save1
    ***Returns***
        Player object with read stats'''
    
    hp,max_hp,xp=0,0,0 # initialize

    f=open(filename).read().split('\n') # open it by line

    # grab each stat from the one letter key
    for line in f:
        if line.split(' ')[0]=='H':
            hp=int(line.split(' ')[1])
        elif line.split(' ')[0]=='M':
            max_hp=int(line.split(' ')[1])
        elif line.split(' ')[0]=='X':
            xp=int(line.split(' ')[1])
    # if the values don't get updated raise an error
    if hp==0 and max_hp==0 and xp==0:
        raise Exception('Load error - player stats not found')
    return(Player(hp,max_hp,xp))


