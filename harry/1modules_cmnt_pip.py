# Programming is a way that tells computer what to do.
# Dynamically typed language, Interpreted & High level language
# Support OOP approach as well as a functional programming approach
# Guido Van rossam in 1991/1989  (Monty Python's Flying Circus show)
# Platform independent , Handle database

# A Jarvis Virtual Assistant
# Love Calculator
# Face Recognition(face direction algorithm)
# Flappy bird game
# Snake game

# Python interpreter ko hum code dete hai jo python script me likha hota hai 
# and vo uss python script ko machine language me change krta hai


# MODULES  (FILE CONTAINING CODE WRITTEN BY SOMEONE ELSE)
#   borrow someone else code in you program (flask , django)
#     1. build in modules (Already shipped with python,no need to install)
#     2. external modules (code written by someone else)

# PIP
#   it is a package manager 
#   pip install modules(like pandas,flask,django)(import pandas,import sklearn(scikit-learn)ML library)
# import pandas       #(PIP)
# import hashlib      #(build in modules)
# import tensorflow   #(EXTERNAL MODULE)

# REPL Read Evaluate Print Loop 

print("Hello world")
print(5)
print("Hi")
                                 
import pyjokes
joke = pyjokes.get_joke()
print(joke)
# Comment
"""
Multi 
line
commment
"""

# 1111(WAP to to print twinkle twinkle little star.)
print("""
Twinkle, twinkle, little star,
How I wonder what you are!
Up above the world so high,
Like a diamond in the sky.

When the blazing sun is gone,
When he nothing shines upon,
Then you show your little light,
Twinkle, twinkle, all the night.

Then the traveler in the dark
Thanks you for your tiny spark,
How could he see where to go,
If you did not twinkle so?

In the dark blue sky you keep,
Often through my curtains peep
For you never shut your eye,
Till the sun is in the sky.

As your bright and tiny spark
Lights the traveler in the dark,
Though I know not what you are,
Twinkle, twinkle, little star.""")

# 2222 (REPL se 5 ka table)

# 3333 (EXTERNAL MODULE)
import pyttsx3
engine = pyttsx3.init()
engine.say("She is Vanshika Bansal and you all must know that She is soo beautiful")
engine.runAndWait()

# 4444(os directory) & 5555(with comments)
import os
# Enter the path of the directory
path = input("Enter directory path: ")
# Get the contents of the directory
contents = os.listdir(path)
# Print the contents
print("Contents of the directory are:")
for item in contents:
    print(item)
