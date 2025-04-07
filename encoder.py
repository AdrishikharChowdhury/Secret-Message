import random
import string

def randomchar():
    return [random.choice(string.ascii_lowercase) for _ in range(3)]

def encoder(message):
    encoded_message=list(message)
    if len(encoded_message)>=3:
        char=encoded_message.pop(0)
        encoded_message.append(char)
        str1=randomchar();
        str2=randomchar();
        encoded_message=str1+encoded_message+str2
    else:
        encoded_message.reverse()
    secret=''.join(encoded_message)
    return secret