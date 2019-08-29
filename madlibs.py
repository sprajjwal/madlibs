#This function takes users input
def pos_input(a, dict):
    dict[a] = input("Enter a " + a + ": ")

#Empty dictionary to hold user input
dict = {
}
pos = ["Adjective 1", "Adjective 2", "Adjective 3", "Adjective 4",
"Adjective 5", "Adjective 6", "Adjective 7", "Animal", "Noun 1",
"Noun 2", "Noun 3", "Part of the body", "Past tense verb",
"Plural noun", "Type of Container"]

#calling input function for every needed POS
for type in pos:
    pos_input(type, dict)

#string with our madlib story
story = '''Old Mother Hubbard went to the %s \nto get her %s %s a bone. \nWhen she got there, the %s was %s, \nAnd so her %s dog had none.
    \n \nJack and Jill went up the %s \nto fetch a %s of water. \nJack fell down and broke his %s \nand Jill came tumbling after. 
    \n \nThere was a girl, and she had a little curl \nRight in the middle of her %s. \nAnd when she was %s, she was very, very %s, 
    \nAnd when she was bad, she was %s. \n \nThere was an %s woman \nWho %s in a shoe. \nShe had so many %s, \nShe didnt know what to do.'''

#printing the final story
print(story %(dict["Noun 1"], dict["Adjective 1"], dict["Animal"], dict["Noun 1"], dict["Adjective 2"], 
dict["Adjective 3"], dict["Noun 2"], dict["Type of Container"], dict["Noun 3"], dict["Part of the body"], dict["Adjective 4"],
dict["Adjective 5"], dict["Adjective 6"], dict["Adjective 7"], dict["Past tense verb"], dict["Plural noun"]))