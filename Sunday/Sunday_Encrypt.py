'''
Program complimentary to Sunday_Decrypt.py. As per the name, this program is an encoder for my Sunday Cipher.
'''

import sys
import time
from tkinter import simpledialog, messagebox


#I WILL conform to 0-based indexing
days = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturaday']
start = 0
start = time.time()

#All following functions basically do the same thing: loop over the days of weeks and index through 
#them until matching letters are found and the letter position is recorded to the list
def first_letter():
    first = []
    for i in range(7):
        for f in range(len(days[i])):
            if days[i][f] == encode_text[0]:
                first.append(f + 1)
    return first


def second_letter():
    fast = first_letter()
    global output
    s2 = set()
    for i in range(7):
        for f in range(len(days[i])):
            if days[i][f] == encode_text[1]:
                for z in range(len(fast)):
                    s2.add(str(fast[z]) + str((f + 1)))
    l2 = [entry for entry in s2]
    output = l2
    return l2


def third_letter():
    fast = second_letter()
    global output
    s3 = set()
    for i in range(7):
        for f in range(len(days[i])):
            if days[i][f] == encode_text[2]:
                for z in range(len(fast)):
                    s3.add(str(fast[z]) + str((f + 1)))
    l3 = [entry for entry in s3]
    output = l3
    return l3


def fourth_letter():
    fast = third_letter()
    global output
    s4 = set()
    for i in range(7):
        for f in range(len(days[i])):
            if days[i][f] == encode_text[3]:
                for z in range(len(fast)):
                    s4.add(str(fast[z]) + str((f + 1)))
    l4 = [entry for entry in s4]
    output = l4
    return l4


def fifth_letter():
    fast = fourth_letter()
    global output
    s5 = set()
    for i in range(7):
        for f in range(len(days[i])):
            if days[i][f] == encode_text[4]:
                for z in range(len(fast)):
                    s5.add(str(fast[z]) + str((f + 1)))
    l5 = [entry for entry in s5]
    output = l5
    return l5


def sixth_letter():
    fast = fifth_letter()
    global output
    s6 = set()
    for i in range(7):
        for f in range(len(days[i])):
            if days[i][f] == encode_text[5]:
                for z in range(len(fast)):
                    s6.add(str(fast[z]) + str((f + 1)))
    l6 = [entry for entry in s6]
    output = l6

if __name__ == '__main__':
#Get our input, validate it and convert it into a list to be broken down by encryption functions
    encoders = {2: second_letter, 3: third_letter, 4:fourth_letter, 5:fifth_letter, 6:sixth_letter}
    encode_text = simpledialog.askstring('Input', 'Enter text to be encoded: ')
    encode_text = encode_text.lower()
    keeper = encode_text
    encode_text = list(encode_text)

    for letters in encode_text:
        if not any(letters in day for day in days):
            print(f'One or more of the characters in "{keeper}" does not exist in any day of the week!')
            sys.exit()

    catch = 0
    try:
        x = 1 / len(encode_text)
        encoders.get(len(encode_text))()
    except ZeroDivisionError:
        messagebox.showerror('YOU CAN\'T FOLLOW INSTRUCTIONS', 'Your input cannot be blank!\nTerminating runtime...')
        catch += 1
    except TypeError:
        messagebox.showerror('YOU CAN\'T FOLLOW INSTRUCTIONS', 'Your input cannot be longer than 5 letters!\nTerminating runtime...')
        catch += 1
    finally:
        if catch:
            sys.exit()
        else:
            #Actual encryption happens here if we pass our exceptions
            messagebox.showwarning('PROCESSING INPUT', 'Thinking...')
            encoders.get(len(encode_text))()

#All possible number combinations that correctly encode the inputted word are stored to combinations.txt
    with open('Sunday/combinations.txt','w') as file:
        file.write(f'{keeper} can be encoded as the following:\n')
        file.writelines(entry + '\n' for entry in output)

#Stats on how many possible combinations were created for the given word and where they were written is displayed
    end = 0
    end = time.time()
    full = end - start
    messagebox.showinfo('Output', f'In {full:.3f} second(s), I calculated {len(output)} possible combinations to encode "{keeper}"!\nAll possible combinations to encode "{keeper}" were saved to combinations.txt')
