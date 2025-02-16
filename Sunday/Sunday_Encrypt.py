'''
Program complimentary to Sunday_Decrypt.py. As per the name, this program is an encoder for my Sunday Cipher.
'''

import sys

days = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturaday']
encode_text = 'test'
keeper = encode_text
encode_text = list(encode_text)

for letter in encode_text:
    if not any(letter in day for day in days):
        print(f'One or more of the letters in "{keeper}" does not exist in any day of the week!')
        sys.exit()


def first_letter():
    global first
    first = []
    num = 0
    for i in range(7):
        for f in range(len(days[i])):
            if days[i][num] == encode_text[0]:
                first.append(num + 1)
            num += 1
        num = 0


def second_letter():
    global s2
    global l2
    global output
    s2 = set()
    num = 0
    for i in range(7):
        for f in range(len(days[i])):
            if days[i][num] == encode_text[1]:
                for z in range(len(first)):
                    s2.add(str(first[z]) + str((num + 1)))
            num += 1
        num = 0
    l2 = [entry for entry in s2]
    output = l2

def third_letter():
    global s3
    global l3
    global output
    s3 = set()
    num = 0
    for i in range(7):
        for f in range(len(days[i])):
            if days[i][num] == encode_text[2]:
                for z in range(len(s2)):
                    s3.add(str(l2[z]) + str((num + 1)))
            num += 1
        num = 0
    l3 = [entry for entry in s3]
    output = l3

def fourth_letter():
    global s4
    global l4
    global output
    s4 = set()
    num = 0
    for i in range(7):
        for f in range(len(days[i])):
            if days[i][f] == encode_text[3]:
                for z in range(len(s3)):
                    s4.add(str(l3[z]) + str((num + 1)))
            num += 1
        num = 0
    l4 = [entry for entry in s4]
    output = l4

def fith_letter():
    global l5
    global output
    s5 = set()
    num = 0
    for i in range(7):
        for f in range(len(days[i])):
            if days[i][f] == encode_text[4]:
                for z in range(len(s4)):
                    s5.add(str(l4[z]) + str((num + 1)))
            num += 1
        num = 0
    l5 = [entry for entry in s5]
    output = l5

def two_letters():
    first_letter()
    second_letter()

def three_letters():
    two_letters()
    third_letter()

def four_letters():
    three_letters()
    fourth_letter()

def five_letters():
    four_letters()
    fith_letter()

#encoding functions are stored in a dictionary to call based on the length of the input
encoders = {2: two_letters, 3: three_letters, 4:four_letters, 5:five_letters}
encoders.get(len(encode_text))()

#All possible number combinations that correctly encode the inputted word are stored to combinations.txt
with open('Sunday/combinations.txt','w') as file:
    file.writelines(entry + '\n' for entry in output)

print(f'There are {len(output)} combinations to encode "{keeper}"!')
print(f'All possible combinations to encode {keeper} were calculated and saved to combinations.txt')