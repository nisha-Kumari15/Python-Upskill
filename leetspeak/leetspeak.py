import random

def leetspeak(mssg):
    leetmessage = ""
    charMapping =  { 'a': ['4', '@', '/-\\'], 'c': ['('], 'd': ['|)'], 'e': ['3'], 'f': ['ph'], 'h': [']-[', '|-|'], 'i': ['1', '!', '|'], 'k': [']<'], 'o': ['0'], 's': ['$', '5'], 't': ['7', '+'], 'u': ['|_|'], 'v': ['\\/']}
    for char in mssg:
        if(char.lower() in charMapping.keys()) and (random.random() <= 0.80):
            possible_replacements = charMapping.get(char.lower(),"")
            leetmessage += random.choice(possible_replacements)
        else:
            leetmessage += char
    return leetmessage


user_input = input("Enter message")
output = leetspeak(user_input)
print("Leetspeak for {} is {}".format(user_input,output))