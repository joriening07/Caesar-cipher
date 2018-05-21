#!/usr/bin/python3
#by three passing protocol,the receiver doesn't need to the key used by the sender.
#Basically, the sender encrypted the message and send to receiver.at this stage
#message has 2 layers of encryption. After receiving the message, 
#receiver encrypted the message by his own key and send back to the sender. Sender decrypted 
#the message and send to receiver again. NOw the message is only encrypted by receiver's key and 
#receiver can simply decrypt it.

import encryptdecrypt as ENC

key1 = int(input(print("please enter the sender's key")))
key2 = int(input(print("please enter the receiver's key")))

user_input = input(print("please enter the text"))
encodekey1 = ENC.encryptText(user_input,key1)
print ("message encoded by sender is :" + encodekey1)
encodekey1key2 = ENC.encryptText(encodekey1,key2)
print ("message encoded by receiver is :" + encodekey1key2)
decodekey1 = ENC.encryptText(encodekey1key2,-key1)
print ("message decoded by sender is :" + decodekey1)
decode = ENC.encryptText(decodekey1,-key2)

print ("The message received is:" + decode)

#END




