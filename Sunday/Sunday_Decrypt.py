'''
Bruteforce decrypter for my Sunday Cipher, originally conceived for my 4546B cryptography challenge for LBC2 2024.
'''

import sys
#nltk.download('words') #YOU NEED THIS LINE ONLY IF YOU HAVE NEVER DOWNLOADED NLTK
from nltk.corpus import words
eng_words = set(words.words()) #Grabs the english dictionary from nltk and puts in a set for faster searching


days = [' sunday', ' monday', ' tuesday', ' wednesday', ' thursday', ' friday', ' saturaday']


#Now the fun begins
l1 = []
set1 = set()
l2 = []
set2 = set()
l3 = []
set3 = set()
l4 = []

def first_letter():
    #Takes the first digit in the cipher text and grabs the corresponding letter from each day of the week and adds them to a list
    starters = []
    for i in range(7):
        if (len(days[i]) - 1) >= cyph_list[0]:
            starters.append(days[i][cyph_list[0]])
    return starters

def two_letters():
    global raw_output
    for i in range(7):
        for f in range(len(first_letter())):
            if (len(days[i]) - 1) >= cyph_list[1]:
                l1.append(first_letter()[f] + days[i][cyph_list[1]])
    raw_output = l1


def three_letters():
    global raw_output
    two_letters()
    for i in range(7):
        for f in range(len(l1)):
            if (len(days[i]) - 1) >= cyph_list[2]:
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
            if (len(days[i]) - 1) >= cyph_list[3]:
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
            if (len(days[i]) - 1) >= cyph_list[4]:
                x = l3[f] + days[i][cyph_list[4]]
                set3.add(x)
    for item in set3:
        l4.append(str(item))
    raw_output = l4


if __name__ == '__main__':

#Input
    cyph_text = input('Enter cipher text (Two or more numbers, maximum 5): ')
#Converts inputted cipher text into a list of integers for indexing purposes
    cyph_list = [int(num) for num in cyph_text if num.isdigit()]

#Dictionary storing the decode functions based on input length. Functions are called from here using the length of cipher text
    decode_functions = {2: two_letters, 3: three_letters, 4: four_letters, 5: five_letters}

#Input validation
    catch = 0
    try:
        vals = [num for num in cyph_text]
        for val in vals:
            x = int(val)
        y = 1 / len(vals)
        decode_functions.get(len(cyph_text))()
    except ValueError:
        print('Your input cannot contain any letters!')
        catch += 1
    except ZeroDivisionError:
        print('Your input cannot be blank!')
        catch += 1
    except TypeError:
        print('Your input must be between 2 and 5 characters. Can you read?')
    finally:
        if catch:
            sys.exit()
        else:
            #Actual decryption happens here if we pass our exceptions
            decode_functions.get(len(cyph_text))()

#Raw output is written to the raw_output.txt file
    with open('Sunday/raw_output.txt','w') as file:
        file.writelines(entry + '\n' for entry in raw_output)

#Creates a list of clean outputs by checking each entry in the raw output against the english dictionary set from nltk
        clean_output = [entry for entry in raw_output if entry in eng_words]

#Writes clean output to the clean_output.txt file
    with open('Sunday/clean_output.txt' , 'w') as file:
        file.writelines(entry + '\n' for entry in clean_output)

    print(f'Done! Raw output ({len(raw_output)} possibilities) was written to raw_output.txt and clean output (checked against a dictionary, {len(clean_output)} possible words) was written to clean_output.txt')