import os
from random import randrange

#Function to randomize the output POS
def random_pos_output(pos_list):
    rand = pos_list[randrange(0, len(pos_list))]
    pos_list.pop(pos_list.index(rand))
    return rand

#Helper function to validate user input
def user_input(pos, index):
    index += 1
    while True:
        word = input("Enter " + pos + " " + str(index) + ": ")
        if word.isalpha():
            return word
        else:
            print("Invalid Input!")

#This function processes user input into the dictionary
def pos_input(pos, pos_dict):
    pos_dict[pos].append(user_input(pos, len(pos_dict[pos]))) 
        
#Empty dictionary to hold user input
pos_dict = {}

#String holding POS that user would input
parts_of_speech = ["Adjective", "Adjective", "Funny Noise", "Funny Noise",
"Noun", "Noun", "Noun", "Noun", "Part of Body", "Place",
"Plural Noun", "Plural Noun"]

#Clears the input page
os.system('clear')

#Welcome screen
print("--------------   WELCOME TO MADLIBS   --------------\n\n\n")

#Calling input function for every needed POS
for pos in parts_of_speech:
    if pos in pos_dict:
        pass
    else:
        pos_dict[pos] = []
    pos_input(pos, pos_dict)


#String with our madlib story
story = '''Almost every community in America now has a bowling %s
because bowling has become very %s with young
%s. Most of them become very %s
at the game. The main object of the game is to roll a heavy bowling
%s.down the alley and knock down the 12 pins
which are at the other end. If you knock them down in one roll, it's
called a %s. If it takes two rolls, it's called
a %s. Many alleys have automatic %s
setters. Others hire %s who set the pins by %s.
The most important thing to remember when bowling is to make
sure you have a good grip on the %s.or you're liable to
drop it on your %s!'''

#Clears the input page
os.system('clear')

#Printing the final story
print(story %(random_pos_output(pos_dict["Place"]), random_pos_output(pos_dict["Adjective"]),
random_pos_output(pos_dict["Plural Noun"]), random_pos_output(pos_dict["Adjective"]),
random_pos_output(pos_dict["Noun"]), random_pos_output(pos_dict["Funny Noise"]),
random_pos_output(pos_dict["Funny Noise"]), random_pos_output(pos_dict["Noun"]),
random_pos_output(pos_dict["Plural Noun"]), random_pos_output(pos_dict["Noun"]), 
random_pos_output(pos_dict["Noun"]), random_pos_output(pos_dict["Part of Body"]) ))