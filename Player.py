from Dice import roll_die
import math

class Player:
    '''this class holds all of the player's stats and actions
    ***Attributes***
        hp: int
            health points
        max_hp: int
            max health
        xp: int
            experience points'''

    def __init__(self, hp, max_hp, xp):
        # these stats go in the save file
        self.hp = hp # health points
        self.max_hp = max_hp # max health
        self.xp = xp # experience points

    
    ### SPELLS

    class Healing_Spell():
        ''' this class belongs to the class of Player to hold a healing spell
        this type of spell is defined separately because it acts differently than spells that deal damage
        *** Attributes***
            dmg: int
                max amount to heal
            aspect='heal': str
                healing spells have a special aspect to change the target in the Fight function
            name: str
                name displayed in CLI
            descr: str
                description displayed on inspect'''

        def __init__(self, dmg, name, descr):
            # in the case of the healing spell "dmg" is actually positive
            self.dmg = dmg # damage
            self.aspect = 'heal' # when this is passed to the Fight function it will cast on the player instead of the opponent
            self.name = name
            self.descr=descr # description
        
        def cast(self,target):
            '''casting the spell for a random amount of healing by dice roll'''
            roll=roll_die(self.dmg)
            new_hp=target.hp + roll 
            # makes it so you can't heal past the hp cap
            if new_hp>target.max_hp:
                target.hp=target.max_hp
            else:
                target.hp=new_hp
            print("You healed "+str(roll)+" hp")


    class Damage_Spell():
        ''' this class belongs to the class of Player to hold most spells
        *** Attributes***
            dmg: int
                max amount of damage
            aspect: str
                represents element associated with spell which makes it more/less effective against elemental enemies
            name: str
                name displayed in CLI
            descr: str
                description displayed on inspect'''
        
        def __init__(self, dmg, aspect, name, descr):
            self.dmg = dmg # damage
            self.aspect = aspect 
            self.name = name
            self.descr=descr # description

        def cast(self,target):
            roll=roll_die(self.dmg)
            if target.weakness==self.aspect and target.weakness!=None:
                # does more damage if the enemy is weak to that
                roll = 2*roll
                print("Super effective! You dealt "+ str(roll) + " dmg")
            elif target.aspect==self.aspect and target.aspect!=None:
                # does less damage to attack enemy with its own aspect
                roll = round(roll/ 2)
                print("Not very effective! You dealt "+ str(roll) + " dmg")
            else:
                print("You dealt "+ str(roll) + " dmg")
            target.hp += - roll
    
            
    ### XP SCALING

    def set_level(self):
        '''sets the player's Level based on the amount of XP, level is used to set max dmg and learn new spells
        ***Returns***
            lvl: int
                starting at 0, gaining 1 level for every 100 XP
                feed to get_actions to get spells for that level'''
        # to make the game more realistic you could implement a nonlinear scaling
        lvl=math.floor(self.xp/100)
        self.max_hp=100 + 50*lvl # increases max health as you level up
        return(lvl)
    
    def get_actions(self):
        '''gets dictionary of spells Player knows with key to cast them
        ALL NEW SPELLS MUST BE DEFINED IN THIS FUNCTION
        ***Returns***
            actions_dict: dict (str,Spell)
                dictionary of spells that can be cast
                feed to actions_input so user can input which to cast
        '''
        lvl=self.set_level() # level determines max efficacy of spells and also how many spells are available
    
        max_heal=10 + 5*lvl
        max_dmg=10 + 5*lvl # makes it so that spells get better as you level up


        ### INITIATING SPELLS

        Heal=self.Healing_Spell(max_heal,'Heal','heals up to ' +str(max_heal)+ ' hp')
        Fire=self.Damage_Spell(max_dmg,'fire','Fireball','deals up to ' +str(max_dmg)+ ' fire damage')
        Ice=self.Damage_Spell(max_dmg,'ice','Ice Blast','deals up to ' +str(max_dmg)+ ' ice damage')
        
        # arrange the spells here in the order to be learned
        spells_list=[Fire,Heal,Ice]

        # this loop adds the spells to the dictionary which match our level
        actions_dict={}
        for i in range(lvl+1):
            if i<len(spells_list):
                actions_dict[str(i)]=spells_list[i]
        return(actions_dict)

    def actions_input(self, actions_dict):
        '''takes user input and corresponds with the in-game spells, continues to prompt input until user enters something valid
        ***Args***
            actions_dict: dict (str, Spell)
                dictionary of spells that can be cast with key for action
                from get_actions
        ***Returns***
            action: str
                spell key or "quit"
                used in Fight function'''

        
        # pull the variables from the class
        actions_list=['quit'] # use this to hold all possible actions
        for key in actions_dict:
            actions_list.append(key) # adding each of the spells

        prompt='' # holds the prompt users will see when they input
        for i in actions_list: # doing this variably will give me flexibility to add new spells as you level up
            if i in actions_dict: # go through actions and add their names
                prompt += i + ' - ' + actions_dict[i].name + ', '
        prompt=prompt[:-2] # remove last comma and space
        
        action='' # to hold the input
        while action not in actions_list: # loop makes it so we keep prompting til we get a valid input
            action=str(input(prompt+'\n'))
            help_word='inspect' # user needs to type this then a space then the number of the action they need help with
            if len(action)>len(help_word): 
                if [action[j]==help_word[j] for j in range(len(help_word))]:
                    if action[len(help_word)+1] in actions_dict:
                        print(actions_dict[action[len(help_word)+1]].descr) # print corresponding descriptions
        return(action)
    