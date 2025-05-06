# SW_Carpentry_Final
Final Project for Software Carpentry Spring 2025

example_main.py contains a short example of how the main game is played

### IMPORTS:

from Player import Player

from Game import Tutorial, Load, Save, Fight

from Enemies import xxxx (choose whichever monsters you want)


### LOADING AND SAVING:
initiate a Player object by calling the Load function on the name of the savefile

call the Save function on a string to write a save to that name

### TUTORIAL:
call Tutorial() to read about how to play a Fight

### FIGHTING:
initiate an Enemy object by calling one of the monsters from the import

call Fight on the Player object and the Enemy object

this will begin the sequence in the Command Line

### NEW ENEMIES:
new enemies can be defined in the Enemies script and then added to the imports

remember to initiate them as an object before calling to fight

### NEW SPELLS:
new spells can either be of the class Healing_Spell or Damage_Spell

they must be initiated within the get_actions function and placed in the variable spells_list in the position corresponding with what level the spell is learned at


