#This function takes users input and validates if its all-alphabets
def pos_input(a, dict):
    while True:
        dict[a] = input("Enter a " + a + ": ")
        if dict[a].isalpha():
            break
        else:
            print("Invalid Input!")

#Empty dictionary to hold user input
dict = {}
pos = ["Adjective 1", "Adjective 2", "Adjective 3", "Adjective 4",
"Adjective 5", "Adjective 6", "Adjective 7", "Animal", "Noun 1",
"Noun 2", "Noun 3", "Part of the body", "Past tense verb",
"Plural noun", "Type of Container"]

#calling input function for every needed POS
for type in pos:
    pos_input(type, dict)


#string with our madlib story
story = '''\n\nOld Mother Hubbard went to the %s 
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

#printing the final story
print(story %(dict["Noun 1"], dict["Adjective 1"], dict["Animal"], 
dict["Noun 1"], dict["Adjective 2"], dict["Adjective 3"], 
dict["Noun 2"], dict["Type of Container"], dict["Noun 3"], 
dict["Part of the body"], dict["Adjective 4"], dict["Adjective 5"], 
dict["Adjective 6"], dict["Adjective 7"], dict["Past tense verb"], 
dict["Plural noun"]))