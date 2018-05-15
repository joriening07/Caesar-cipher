#!/usr/bin/python3
#encrypdecrypt.py

#takes the input_text and encrypts it, returning the result

def encryptText(input_text,key):
    input_text = input_text.upper()
    result = ""
    for letter in input_text:
        #get the ASCII for the character
        ascii_value = ord(letter)
        #exclude the non-character ones
        if (ascii_value < ord('A')) or (ascii_value > ord('Z')):
            result+=letter
        else:
            #apply the encryption key
            key_value = ascii_value + key
            if not(ord('A') < key_value < ord('Z')):
                key_value = ord('A') + (key_value - ord('A'))%26 
            #adding the encryped letter to the result string
            result += str(chr(key_value))
    return result

#Test function
def main():
    print ("Please enter text to scramble:")
#get user input
    try:
        user_input = input()
        scrambled_result = encryptText(user_input,10)
        print ('result:' + scrambled_result)
        print ('To un-scramble, press enter again')
        input()
        unscrambled_result = encryptText(scrambled_result,-10)
        print ('result:' + unscrambled_result)
    except UnicodeDecodeError:
        print ('Sorry, only ASCII Characters are supported')

main()
#end
        
