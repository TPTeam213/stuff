'''
Program complimentary to Sunday_Decrypt.py. As per the name, this program is an encoder for my Sunday Cipher.
'''

import sys
import time

#I WILL conform to 0-based indexing
days = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturaday']
start = time.time()

def first_letter():
    first = []
    num = 0
    for i in range(7):
        for f in range(len(days[i])):
            if days[i][f] == encode_text[0]:
                first.append(f + 1)
            num += 1
        num = 0
    return first


def second_letter():
    fast = first_letter()
    global output
    s2 = set()
    num = 0
    for i in range(7):
        for f in range(len(days[i])):
            if days[i][f] == encode_text[1]:
                for z in range(len(fast)):
                    s2.add(str(fast[z]) + str((f + 1)))
            num += 1
        num = 0
    l2 = [entry for entry in s2]
    output = l2
    return l2


def third_letter():
    fast = second_letter()
    global output
    s3 = set()
    num = 0
    for i in range(7):
        for f in range(len(days[i])):
            if days[i][f] == encode_text[2]:
                for z in range(len(fast)):
                    s3.add(str(fast[z]) + str((f + 1)))
            num += 1
        num = 0
    l3 = [entry for entry in s3]
    output = l3
    return l3


def fourth_letter():
    fast = third_letter()
    global output
    s4 = set()
    num = 0
    for i in range(7):
        for f in range(len(days[i])):
            if days[i][f] == encode_text[3]:
                for z in range(len(fast)):
                    s4.add(str(fast[z]) + str((f + 1)))
            num += 1
        num = 0
    l4 = [entry for entry in s4]
    output = l4
    return l4


def fifth_letter():
    fast = fourth_letter()
    global output
    s5 = set()
    num = 0
    for i in range(7):
        for f in range(len(days[i])):
            if days[i][f] == encode_text[4]:
                for z in range(len(fast)):
                    s5.add(str(fast[z]) + str((f + 1)))
            num += 1
        num = 0
    l5 = [entry for entry in s5]
    output = l5
    return l5


def sixth_letter():
    fast = fifth_letter()
    global output
    s6 = set()
    num = 0
    for i in range(7):
        for f in range(len(days[i])):
            if days[i][f] == encode_text[5]:
                for z in range(len(fast)):
                    s6.add(str(fast[z]) + str((f + 1)))
            num += 1
        num = 0
    l6 = [entry for entry in s6]
    output = l6

if __name__ == '__main__':
#Get our input, validate it and convert it into a list to be broken down by encryption functions
    encoders = {2: second_letter, 3: third_letter, 4:fourth_letter, 5:fifth_letter, 6:sixth_letter}
    encode_text = input('Enter text to be encoded: ')
    keeper = encode_text
    encode_text = list(encode_text)

    for letters in encode_text:
        if not any(letters in day for day in days):
            print(f'One or more of the characters in "{keeper}" does not exist in any day of the week!')
            sys.exit()

    catch = 0
    try:
        x = 1 / len(encode_text)
    except ZeroDivisionError:
        print('Your input cannot be blank!')
        catch += 1
    except TypeError:
        print('Your input cannot be longer than 5 letters!')
        catch += 1
    finally:
        if catch:
            sys.exit()
        else:
            #Actual encryption happens here if we pass our exceptions
            print('Thinking...')
            encoders.get(len(encode_text))()

#All possible number combinations that correctly encode the inputted word are stored to combinations.txt
    with open('Sunday/combinations.txt','w') as file:
        file.write(f'{keeper} can be encoded as the following:\n')
        file.writelines(entry + '\n' for entry in output)

#Stats on how many possible combinations were created for the given word and where they were written is displayed
    end = time.time()
    full = end - start
    print(f'In {full:.3f} second(s), I calculated {len(output)} possible combinations to encode "{keeper}"!')
    print(f'All possible combinations to encode "{keeper}" were calculated and saved to combinations.txt')