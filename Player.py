from Dice import roll_die

class Player:
    def __init__(self, hp, max_hp, xp):
        self.hp = hp # health points
        self.max_hp = max_hp # max health
        self.xp = xp # experience points

    ### Implement level up system
    
    class Spell(): # parent class for the other Spells to inherit from
        def __init__(self, dmg, aspect, name, descr):
            self.dmg = dmg # damage
            self.aspect = aspect 
            self.name = name
            self.descr=descr # description
    
    class Healing_Spell(Spell):
        def __init__(self, dmg, aspect, name, descr):
            super.__init__(dmg, aspect, name, descr)
        
        def cast(self,target):
            roll=roll_die(self.dmg)
            new_hp=target.hp+roll
            # makes it so you can't heal past the hp cap
            if new_hp>target.max_hp:
                target.hp=target.max_hp
            else:
                target.hp=new_hp
            print("You healed "+str(roll)+" hp")


    class Fire_Spell(Spell):
        def __init__(self, dmg, aspect, name, descr):
            super.__init__(dmg, aspect, name, descr)
        
        def cast(self,target):
            roll=roll_die(self.dmg)
            if target.weakness==self.aspect:
                # does more damage if the enemy is weak to that
                roll = 2*roll
                print("Super effective! You dealt "+ str(roll) + " dmg")
            else:
                print("You dealt "+ str(roll) + " dmg")
            target.hp += - roll
            
    # here we can implement the xp thing
    Heal=Healing_Spell(8,'heal','Heal','heals small amount of hp')
    Fire=Fire_Spell(8,'fire','Fireball','does small amount of fire damage')

    actions_dict={'0':Heal,'1':Fire} # dictionary for actions represented with numbers
    actions_list=['quit'] # use this to hold all possible actions
    for key in actions_dict:
        actions_list.append(key) # adding each of the spells

    def actions_input(self):
        '''takes user input and corresponds with the in-game function
        also continues to prompt input until user enters something valid'''

        # pull the variables from the class
        actions_dict=self.actions_dict
        actions_list=self.actions_list 

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
    