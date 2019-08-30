import os
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
parts_of_speech = ["Adjective", "Adjective", "Adjective", "Adjective",
"Adjective", "Adjective", "Adjective", "Animal", "Noun",
"Noun", "Noun", "Part of the body", "Past tense verb",
"Plural noun", "Type of Container"]

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
story = '''Old Mother Hubbard went to the %s 
to get her %s %s a bone. 
When she got there, the %s was %s, 
And so her %s dog had none.
    
Jack and Jill went up the %s 
to fetch a %s of water. 
Jack fell down and broke his %s 
and Jill came tumbling after. 

There was a girl, and she had a little curl 
Right in the middle of her %s. 
And when she was %s, she was very, very %s, 
And when she was bad, she was %s.

There was an %s woman 
Who %s in a shoe. 
She had so many %s, 
She didnt know what to do.'''

#Clears the input page
os.system('clear')

#Printing the final story
print(story %(pos_dict["Noun"][0], pos_dict["Adjective"][0], pos_dict["Animal"][0], 
pos_dict["Noun"][0], pos_dict["Adjective"][1], pos_dict["Adjective"][2], 
pos_dict["Noun"][1], pos_dict["Type of Container"][0], pos_dict["Noun"][2], 
pos_dict["Part of the body"][0], pos_dict["Adjective"][3], pos_dict["Adjective"][4], 
pos_dict["Adjective"][5], pos_dict["Adjective"][6], pos_dict["Past tense verb"][0], 
pos_dict["Plural noun"][0]))