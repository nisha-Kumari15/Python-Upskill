import random

def decrypt_leetspeak(mssg):
    decrypt = mssg
    charMapping =  { 'a': ['4', '@', '/-\\'], 'c': ['('], 'd': ['|)'], 'e': ['3'], 'f': ['ph'], 'h': [']-[', '|-|'], 'i': ['1', '!', '|'], 'k': [']<'], 'o': ['0'], 's': ['$', '5'], 't': ['7', '+'], 'u': ['|_|'], 'v': ['\\/']}
    for key in charMapping.keys():
        for value in charMapping[key]:
            if value in decrypt:
                decrypt = decrypt.replace(value,key)
    return decrypt

user_input = input("Enter message")
output = decrypt_leetspeak(user_input)
print("Decrypt_Leetspeak for {} is {}".format(user_input,output))
