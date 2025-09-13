Designed and written by Ben Frederick for CS1210H at The University of Vermont. Idea originally conceived for the infamous "4546B" cryptography challenge presented in LBC2024.

Sunday_Decrypt.py:

This program brute-force decrypts Sunday Cipher text, with a maximum length of 6, and generates all possibilities and writes them to the raw_output.txt file. Raw output is checked against an english dictionary and this new output is written to the clean_output.txt file. The program depends on the sys, time, tkinter, and nltk pip installable modules to run properly. See line 10 for a specific note on ntlk downloading. To use this program, simply run the file and follow the on-screen dialogue prompts. If the program encounters an error, it will quit, and you must run the file again (Pay attention to your input).

Sunday_Encrypt.py:


This program is the compliment to Sunday_Decrypt.py and will encrypt a given string, with a maximum length of 6, with th Sunday Cipher. All possibilities are written to the combinations.txt file. The program depends on the pip installable modules sys, time, and tkinter to run properly. To use this program, simply run the file and follow the on-screen dialogue prompts. If the program encounters an error, it will quit, and you must run the file again (Pay attention to your input).
