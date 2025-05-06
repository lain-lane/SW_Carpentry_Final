import unittest
from Player import Player
from Enemies import Enemy

class Test_Heal(unittest.TestCase):
    def test_1(self):
        # test that it doesn't heal past max
        Joe=Player(10,10,0)
        Heal=Player.Healing_Spell(10,'Heal','heals up to 10 hp')
        Heal.cast(Joe)
        self.assertTrue(Joe.hp<=Joe.max_hp)
    
    def test_2(self):
        # test that it actually raises his health
        old_hp=5
        Joe=Player(old_hp,10,0)
        Heal=Player.Healing_Spell(5,'Heal','heals up to 5 hp')
        Heal.cast(Joe)
        self.assertTrue(Joe.hp>=old_hp)

class Test_Damage(unittest.TestCase):
    def test_1(self):
        # test that player does damage to enemies
        Attack=Player.Damage_Spell(10,None,'Attack','deals up to 10 dmg')
        old_hp=100
        Evil_Joe=Enemy(old_hp,0,0,None,None,'Evil Joe')
        Attack.cast(Evil_Joe)
        self.assertTrue(Evil_Joe.hp<=old_hp)

    def test_2(self):
        # test that enemies do damage to player
        Evil_Joe=Enemy(10,10,0,None,None,'Evil Joe')
        old_hp=100
        Joe=Player(old_hp,100,0)
        Evil_Joe.attack(Joe)
        self.assertTrue(Joe.hp<=old_hp)

class Test_XP(unittest.TestCase):
    def test_1(self):
        # test that killing enemies drops xp
        Joe=Player(100,100,0)
        Evil_Joe=Enemy(10,0,10,None,None,'Evil Joe')
        Evil_Joe.die(Joe)
        self.assertTrue(Joe.xp==10)

    def test_2(self):
        # test level up
        Joe=Player(100,100,1000)
        self.assertTrue(Joe.set_level()==10)


if __name__=='__main__':
    unittest.main()
