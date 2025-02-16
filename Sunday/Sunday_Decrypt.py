'''
Bruteforce decrypter for my Sunday Cipher, originally conceived for my 4546B cryptography challenge for LBC2 2024.
'''

import nltk
#nltk.download('words') #YOU NEED THIS LINE ONLY IF YOU HAVE NEVER DOWNLOADED NLTK
from nltk.corpus import words
eng_words = set(words.words()) #Grabs the english dictionary from nltk and puts in a set for faster searching


days = [' sunday', ' monday', ' tuesday', ' wednesday', ' thursday', ' friday', ' saturaday']
cyph_text = input('Enter cipher text: ')

assert cyph_text != ''

#Converts inputted cipher text into a list of integers for indexing purposes
cyph_list = [int(num) for num in cyph_text if num.isdigit()]

#takes the first digit in the cipher text and grabs the corresponding letter from each day of the week and adds them to a list
starters = []
for i in range(7):
        starters.append(days[i][cyph_list[0]])

#Now the fun begins
l1 = []
set1 = set()
l2 = []
set2 = set()
l3 = []
set3 = set()
l4 = []

def two_letters():
    global raw_output
    for i in range(7):
        for f in range(7):
            l1.append(starters[f] + days[i][cyph_list[1]])
    raw_output = l1

def three_letters():
    global raw_output
    two_letters()
    for i in range(7):
        for f in range(len(l1)):
            x = l1[f] + days[i][cyph_list[2]]
            set1.add(x)
    for item in set1:
        l2.append(str(item))
    raw_output = l2        

def four_letters():
    global raw_output
    three_letters()
    for i in range(7):
        for f in range(len(l2)):
            x = l2[f] + days[i][cyph_list[3]]
            set2.add(x)
    for item in set2:
        l3.append(str(item))
    raw_output = l3

def five_letters():
    global raw_output
    four_letters()
    for i in range(7):
        for f in range(len(l3)):
            x = l3[f] + days[i][cyph_list[4]]
            set3.add(x)
    for item in set3:
        l4.append(str(item))
    raw_output = l4

#Dictionary storing the decode functions based on input length. Functions are called from here using the length of cipher text
decode_functions = {2: two_letters, 3: three_letters, 4: four_letters, 5: five_letters}
decode_functions.get(len(cyph_text))()

#Raw output is written to the raw_output.txt file
with open('Sunday/raw_output.txt','w') as file:
    file.writelines(entry + '\n' for entry in raw_output)

#Creates a list of clean outputs by checking each entry in the raw output against the english dictionary set from nltk
clean_output = [entry for entry in raw_output if entry in eng_words]

#Writes clean output to the clean_output.txt file
with open('Sunday/clean_output.txt' , 'w') as file:
    file.writelines(entry + '\n' for entry in clean_output)

print('Done! Raw output was written to raw_output.txt and clean output (checked against a dictionary) was written to clean_output.txt')