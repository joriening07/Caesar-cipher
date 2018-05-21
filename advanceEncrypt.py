#!/usr/bin/python3
#this scritp will encrypt the text every 5 elemnets by key,key+1,key+2....

import encryptdecrypt as Enc


print ("Please enter the text:")
#get the input
user_input = input()
key = 1
n = len(user_input)
print (n) 
m = n//5
print (m)
t=0
result = ""
original = ""
for i in range(0,m):
    if t<m: 
        encode_5El= Enc.encryptText(user_input[0+5*t:5+5*t],key)        
        original += Enc.encryptText(encode_5El,-key)        
        result += encode_5El
        key += 1
        t += 1
    else:
        break
result += Enc.encryptText(user_input[5*m:n],key)
original += Enc.encryptText(result[5*m:n],-key)

print ("the encode text:" + result)
print ("the decoded text:" + original)
