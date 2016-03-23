
###############################################################################
#
# Filename: morsecode1.py
#
# CS Assignment: Programming Project Ch 9 exercise 21
# Text: The Practice of Computing with Python
#
# Version History
#
# Date:       Name:                ChangeNo:  Comment:
# 03/22/2016  Matthew Lopez        00000000    Create Algorithm  
# 03/22/2016  Matthew Lopez        00000001    Create dictionaries and main code 
# 03/22/2016  Matthew Lopez        00000002    Final Cleanup and more testing
#
#
# Problem Description: 
#
# Complete Chapter 9, exercise 21, with the following modifications: the program
# is to calculate error detection values for a message and encrypt both the
# message and error detection codes into Morse-code.The message will be sent to
# another student via e-mail as a .txt file attachment. The received e-mail file
# (.txt file attachment) will be unencrypted and checked using the error
# detection code. Thus, your program must be able to encrypt and decrypt
# Morse-code, while performing the error detection.
#
###############################################################################
#
# Pseudocode Algorithm:
#
# - Establish dictionaries for English characters to Morse Code and vice versa
# - Define checksum to verify integrity of message transmission
# - Prompt user for what they want to encrypt
# - Encode user input and export as text file
# - Retrieve text file and decode message into a text file
#
###############################################################################
#
# Inputs: System Keyboard
# Outputs: System Console
#
###############################################################################

import re

# Establish dictionary for alphabetical letters and grammer syntex translation
# to morse code

reg_dict = {'A':'.-', 'B': '-...','C':'-.-.','D':'-..','E':'.', 'F':'..-.',
            'G':'--.','H':'....','I':'..','J':'.---','K':'-.-','L':'.-..', 'M':'--',
            'N':'-.','O':'---','P':'.--.','Q':'--.-','R':'.-.', 'S':'...','T':'-',
            'U':'..-','V':'...-','W':'.--','X':'-..-','Y':'-.--','Z':'--..','0':'-----',
            '1':'.----','2':'..---','3':'...--','4':'....-','5':'.....','6':'-....',
            '7':'--...','8':'---..','9':'----.','.':'.-.-.-',',':'--..--',':':'---...',
            '': '','   ': '   ','       ': '       ','_': '','  ': ' ','       \n': '\n'}
# Establish dictionary for morse code translation to alphabetical letters and
# grammer syntex
morse_dict = dict(zip(reg_dict.values(), reg_dict.keys()))
        
def initial_query ():
    x_input = []
    user_entry = input("Type message (CAPS), when done type 'Finished': ")
    while user_entry != "Finished":
        x_input.append(user_entry)
        user_entry = input("")
    return x_input

##################### Checksum from Dr. Steve Powelson #########################

def create_checksum (goesinta):
  checksum = 0                                # Initialize the Checksum value
  for position, character in enumerate(goesinta, 1):  
    character_num = ord(character)            # Define the integer equivalent of the character
    check_val = position * character_num      # Determine the characters check value
    checksum += check_val                     # Accumulate the check values
  goesouta = checksum
  return str(goesouta)

##################### Code referrenced from Israel Rosales #####################

def encode_morse():
    text_position = 0                        # Define position of text
    user_input = ""
    morse_encrypt = ""
    y_input = initial_query()
    encode_file = open("message.txt", "w")   # Open file to encrypt
    for line in y_input[:]:
        line_checksum = str(create_checksum(line)) # Encrypt checksum for line
        user_input = y_input[text_position] + "   " + line_checksum
        for each_word in user_input.split():    # Split each word individually
            for each_character in each_word:
                each_character = each_character.upper() # Ensure each letter is uppercase
                morse_encrypt += reg_dict[each_character] + "   "
            morse_encrypt += "    "         # End of each line
        morse_encrypt += "\n"               # Encrypt each neew line
        text_position += 1
    encode_file.write(morse_encrypt)
    print(morse_encrypt)                    # Print encrypted text (MorseCode)

def decode_morse(x_file):
    text_position = 0
    decode_list = []                        # Empty list for dynamic input
    decode_text = ""
    decode_encrypt = ""
    buddy_file = open(x_file, "r")          # Read encrypted file
    for line_decode in iter(buddy_file):
        decode_list.append(line_decode)
    for morse_line in decode_list[:]:
        decode_text = decode_list[text_position]
        decode_split = re.split(r'(\s+)', decode_text)
        for morse_decoder in decode_split:
            decode_to_text += reg_dict[morse_decoder]
        text_position += 1
    file_output = open("Decoded Text.txt", "w")
    file_output.write(decode_to_text)
    print(decode_to_text)

encode_or_decode = input("To Encrypt message, enter 'Encrypt'. To Decrypt message enter 'Decrypt': ")
if encode_or_decode == "Decrypt":
    which_file = input("Enter the name of the file you would like to be decrypted: ")
    decode_filename = which_file + ".txt"
    decode_morse(decode_filename)
elif encode_or_decode == "Encrypt":
    encode_morse()
else:
    print("Prompted command cannot be executed. Ending program.")
