# -*- coding: utf-8 -*-
"""
Created on Wed Jun 16 13:17:17 2021

@author: Michael
"""


adjective1 = str(input('Enter an Adjective: '))
adjective2 = str(input('Enter an Adjective: '))
bird = str(input('Enter a type of bird: '))
room = str(input('Enter a room in a house: '))
verb1 = str(input('Enter a past tense verb: '))
verb2 = str(input('Enter a verb: '))
name = str(input('Enter a relative\'s name: '))
noun1 = str(input('Enter a noun: '))
liquid = str(input('Enter a liquid: '))
verb3 = str(input('Enter a verb ending in -ing: '))
bodypart = str(input('Enter a body part (plural): '))
noun2 = str(input('Enter a plural noun: '))
verb4 = str(input('Enter a verb ending in -ing: '))
noun3 = str(input('Enter a noun: '))

story = "It was a " + adjective1 + ", cold November day. I woke up to the " + adjective2 + " smell of "\
+ bird + " roasting in the " + room + " downstairs. I " + verb1 + " down the stairs to see if I could help "\
+ verb2 + " the dinner. My mom said, \"See if " + name + " needs a fresh " + noun1 + "\" So I carried a tray of glasses full of "\
+ liquid + " into the " + verb3 + " room. When I got there, I couldn\'t believe my " + bodypart \
+ "! There were " + noun2 + " " + verb4 + " on the " + noun3 +"!"
 
print(story)
