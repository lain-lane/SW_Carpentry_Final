import random


### defining basic classes
class Player:
    def __init__(self, hp, xp, weapon):
        self.hp = hp
        self.xp = xp # need to use this with some leveling system to learn spells
        self.weapon = weapon

    def attack(self, enemy):
        critchance=.50 + .01*self.xp
        roll=random.uniform(0,1)
        if roll>=critchance:
            damage=round(random.gauss(1.5*self.weapon.dmg,0.1*self.weapon.dmg))
            while (1.4*self.weapon.dmg <= damage <= 1.6*self.weapon.dmg)==False: # rerolls the randomizer if it's not within the range
                damage=round(random.gauss(1.5*self.weapon.dmg,0.1*self.weapon.dmg))
            crit=True
        else:
            damage = round(random.gauss(self.weapon.dmg,0.2*self.weapon.dmg))
            while (0.8*self.weapon.dmg <= damage <= 1.2*self.weapon.dmg)==False: # rerolls the randomizer if it's not within the range
                damage=round(random.gauss(self.weapon.dmg,0.2*self.weapon.dmg))
            crit=False
        enemy.hp += - damage
        return(damage,crit)


class Enemy:
    # realizing I could have made some parent class for things that have hp which enemy and player would inherit from
    # but that's not what I did and it's too late now
    def __init__(self, hp, dmg):
        self.hp = hp
        self.dmg = dmg

    def attack(self, player): 
        damage = round(random.gauss(self.dmg,0.2*self.dmg))
        player.hp += - damage
        return(damage)
    

class Weapon:
    # I called this weapon but I actually wanna streamline the concept and make it based on learning spells
    # don't want to make a whole currency shop system that's gonna take too long
    # real Kodu hours we on some Scubo shit boys
    def __init__(self, dmg, aspect):
        self.dmg = dmg
        self.aspect=aspect # use this to make some enemies weaker to a type

    
def Fight(player, enemy): 
        whiteflag=False
        quitter=False
        turn_counter=1 # player goes first (positive), enemy's turn will be negative

        actions_dict={'0':player.attack(enemy)}
        
        while player.hp>0 and enemy.hp>0 and whiteflag==False and quitter==False:
            if turn_counter<0: # enemy turn
                print('Enemy HP: '+ str(enemy.hp))
                if enemy.hp<10: # this is a retreat behavior not all enemies will have this
                    whiteflag=True 
                    print('enemy ran away')
                
                else:
                    damage=enemy.attack(player)
                    print('he dealt ' + str(damage)+ ' dmg')
                    turn_counter=-turn_counter

            else:
                # player turn
                print('Your HP: '+ str(player.hp))
                action=actions_input()
                # now this calls on the function which ensures they enter a valid input
                # we can code all of the spells here in the fight section and have conditionals in the 
                # action input so that they can only see the spells they've learned
                if action=='0':
                    damage,crit=actions_dict[action]
                    if crit==False:
                        print('you dealt ' + str(damage)+ ' dmg')
                    else:
                        print('critical hit! '+'you dealt ' + str(damage)+ ' dmg')
                elif action=='1':
                    whiteflag=True
                    print('you ran away')
                elif action=='quit':
                    quitter=True
                turn_counter=-turn_counter

        if enemy.hp<=0:
            print('he died')
        elif player.hp<=0:
            print('you died')

def Game():
    print('Welcome to the game!\n')
    # make this have a while loop that keeps the game going until user types quit
    pass

def actions_input():
    actions_dict={'0':['attack','damage opponent'],'1':['retreat','leave the fight']} # dictionary for actions represented with numbers
    actions_list=['quit'] # all possible actions
    for key in actions_dict:
        actions_list.append(key)

    prompt='' # to hold the prompt users will see when they input
    for i in actions_list: 
        if i in actions_dict: # go through actions and add their descriptions
            prompt += i + ' - ' + actions_dict[i][0] + ', '
    prompt=prompt[:-2] # remove last comma and space
    
    action='' # to hold the input
    while action not in actions_list: # loop makes it so we keep prompting til we get a valid input
        action=str(input(prompt+'\n'))
        help_word='inspect' # user needs to type this then a space then the number of the action they need help with
        if len(action)>len(help_word):
            if [action[j]==help_word[j] for j in range(len(help_word))]:
                if action[len(help_word)+1] in actions_dict:
                    print(actions_dict[action[len(help_word)+1]][1]) # print corresponding descriptions
    return(action)



if __name__=='__main__':

    sword=Weapon(5,None)
    Joe=Player(100,0,sword)
    Evil_Joe=Enemy(100,5)
    Fight(Joe,Evil_Joe)





