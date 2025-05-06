import random

class Enemy:
    def __init__(self, hp, dmg, drop,weakness,name):
        self.hp = hp # health points
        self.dmg = dmg # attack damage
        self.drop = drop # experience drop
        self.weakness = weakness
        self.name = name

    def attack(self, player): 
        damage = round(random.gauss(self.dmg,0.2*self.dmg))
        player.hp += - damage
        return(damage)
    
    def die(self, opponent):
        opponent.xp += self.drop

Goblin=Enemy(50,5,10,None,"Goblin")

Dragon=Enemy(1000,50,1000,'arcane',"Dragon")

Snow_Golem=Enemy(100,20,50,'fire',"Snow Golem")

Magma_Cube=Enemy(10,2,4,'ice','Magma Cube')