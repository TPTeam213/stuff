'''
Bruteforce decrypter for my Sunday Cipher, originally conceived for my magnum opus 4546B cryptography challenge for LBC2 2024, available on my GitHub 'stuff' repos.
'''

import sys
import time
from tkinter import simpledialog, messagebox

#nltk.download('words') #YOU NEED THIS LINE ONLY IF YOU HAVE NEVER DOWNLOADED NLTK
from nltk.corpus import words
eng_words = set(words.words()) #Grabs the english dictionary from nltk and puts in a set for faster searching

start_t = 0
start_t = time.time()
#I will NOT conform to 0-based indexing
days = [' sunday', ' monday', ' tuesday', ' wednesday', ' thursday', ' friday', ' saturaday']


#Now the fun begins (redundant sequences)
    #It has to be done like this trust me there is no more efficient way
        #Trust
l1 = []
set1 = set()
l2 = []
set2 = set()
l3 = []
set3 = set()
l4 = []
set4 = set()
l5 = []

def first_letter():
    #Takes the first digit in the cipher text and grabs the corresponding letter from each day of the week and 
    # adds them to a list
    starters = []
    for i in range(7):
        if (len(days[i]) - 1) >= cyph_list[0]:
            starters.append(days[i][cyph_list[0]])
    return starters

#All following functions basically do the same thing: loop over the days of weeks and index them on the given number 
# and adds to a growing collection of possible words
def two_letters():
    global raw_output
    l1.clear()
    for i in range(7):
        for f in range(len(first_letter())):
            if (len(days[i]) - 1) >= cyph_list[1]:
                l1.append(first_letter()[f] + days[i][cyph_list[1]])
    raw_output = l1


def three_letters():
    global raw_output
    #Clear all our sequences just to completely avoid spillover from previous program runs (this did happen to me once while testing)
    two_letters()
    set1.clear()
    l2.clear()
    #Loop over all 7 days of the week
    for i in range(7):
        #Each combination in the previous sequence is combined with all new possible next letters
        for f in range(len(l1)):
            #If the number is smaller than the length of the day week, we can do our indexing and adding
            if (len(days[i]) - 1) >= cyph_list[2]:
                #Here's the juice. Each existing "word" is combined with the new letter for each day of the week
                x = l1[f] + days[i][cyph_list[2]]
                set1.add(x)
    #New sequence is duplicated to a list for indexing in future functions
        #This seems redundant, but it's actually faster than manually checking for dupes becuase of how fast sets are read 
    for item in set1:
        l2.append(str(item))
    raw_output = l2


def four_letters():
    global raw_output
    three_letters()
    set2.clear()
    l3.clear()
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
    set3.clear()
    l4.clear()
    for i in range(7):
        for f in range(len(l3)):
            if (len(days[i]) - 1) >= cyph_list[4]:
                x = l3[f] + days[i][cyph_list[4]]
                set3.add(x)
    for item in set3:
        l4.append(str(item))
    raw_output = l4


def six_letters():
    global raw_output
    five_letters()
    set4.clear()
    l5.clear()
    for i in range(7):
        for f in range(len(l4)):
            if (len(days[i]) - 1) >= cyph_list[5]:
                x = l4[f] + days[i][cyph_list[5]]
                set4.add(x)
    for item in set4:
        l5.append(str(item))
    raw_output = l5


if __name__ == '__main__':
#Input
    cyph_text = simpledialog.askstring('Input', 'Enter cipher text (Two or more numbers, maximum 6): ')
#Dictionary storing the decode functions based on input length. Functions are called from here using the length of cipher text
    decode_functions = {2: two_letters, 3: three_letters, 4: four_letters, 5: five_letters, 6: six_letters}

#Input validation
    catch = 0
    try:
        cyph_list = [int(num) for num in cyph_text]
        y = 1 / len(cyph_list)
        decode_functions.get(len(cyph_text))()
    except ValueError:
        messagebox.showerror('YOU CAN\'T FOLLOW INSTRUCTIONS', 'Your input cannot contain any letters!\nTerminating runtime...')
        catch += 1
    except ZeroDivisionError:
        messagebox.showerror('YOU CAN\'T FOLLOW INSTRUCTIONS', 'Your input cannot be blank! Seriously?\nTerminating runtime...')
        catch += 1
    except TypeError:
        messagebox.showerror('YOU CAN\'T FOLLOW INSTRUCTIONS', 'Your input must be between 2 and 6 characters. Can you read?\nTerminating runtime...')
        catch += 1
    finally:
        if catch:
            sys.exit()
        else:
            #Converts inputted cipher text into a list of integers for indexing purposes
            cyph_list = [int(num) for num in cyph_text]
            messagebox.showwarning('PROCESSING INPUT', 'Thinking...') #cogito ergo sum
            #Actual decryption happens here if we pass our exceptions
            decode_functions.get(len(cyph_text))()


#Raw output is written to the raw_output.txt file
    with open('Sunday/raw_output.txt' , 'w') as file:
        file.write(f'{cyph_text} can decode into the following:\n')
        file.writelines(entry + '\n' for entry in raw_output)

#Creates a list of clean outputs by checking each entry in the raw output against the english dictionary set from nltk
    clean_output = [entry for entry in raw_output if entry in eng_words]

#Writes clean output to the clean_output.txt file
    with open('Sunday/clean_output.txt' , 'w') as file:
        file.write(f'{cyph_text} can decode into the following:\n')
        file.writelines(entry + '\n' for entry in clean_output)

    end_t = 0
    end_t = time.time()
    #Total run time is calculated
    elapsed = end_t - start_t
    messagebox.showinfo('Output', f'Done!\n In {elapsed:.3f} second(s), I calculated {len(raw_output):,} possibilities. This raw output was written to raw_output.txt and clean output (checked against a dictionary, {len(clean_output):,} pottential words) was written to clean_output.txt \n')