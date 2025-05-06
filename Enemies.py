import random

class Enemy:
    '''this class holds stats for an enemy to Fight in the game
    ***Attributes***
        hp: int
            health points
        dmg: int
            average attack damage
        drop: int
            amount of xp given to player when killed
        aspect: str
            for elemental enemies
            spells are weaker if aspect matches the enemy's aspect
        weakness: str
            spells are stronger if aspect matches the enemy's weakness
        name: str
            displayed in Fight '''
    
    def __init__(self, hp, dmg, drop,aspect,weakness,name):
        self.hp = hp # health points
        self.dmg = dmg # attack damage
        self.drop = drop # experience drop
        self.aspect = aspect
        self.weakness = weakness
        self.name = name

    def attack(self, player): 
        '''deals random amount of damage to player around average value
        ***Args***
            player: Player
                player object to whom damage is dealt in Fight'''
        # deals random amount of damage around average value
        # I could make this a dice roll too but its fine
        damage = round(random.gauss(self.dmg,0.2*self.dmg))
        player.hp += - damage
        return(damage)
    
    def die(self, opponent):
        '''gives dropped xp to opponent
        ***Args***
            opponent: Player
                player object from the Fight'''
        opponent.xp += self.drop

Goblin=Enemy(50,5,10,None,None,"Goblin")

Dragon=Enemy(1000,50,1000,None,'arcane',"Dragon")

Snow_Sprite=Enemy(20,5,5,'ice','fire','Snow Sprite')

Snow_Golem=Enemy(100,20,50,'ice','fire',"Snow Golem")

Magma_Cube=Enemy(10,2,4,'fire','ice','Magma Cube')