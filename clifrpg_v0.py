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

        actions_dict={'0',player.attack}
        
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
                action=str(input('0 - attack, 1 - retreat\n'))
                # change this so that it calls on a dictionary of possible inputs
                if action=='0':
                    damage,crit=player.attack(enemy)
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





if __name__=='__main__':

    sword=Weapon(5,None)
    Joe=Player(100,0,sword)
    Evil_Joe=Enemy(100,5)
    Fight(Joe,Evil_Joe)



