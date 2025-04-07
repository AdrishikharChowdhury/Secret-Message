def decoder(message):
    decoded_message=list(message)
    if len(decoded_message)<3:
        decoded_message.reverse()
        secret=''.join(decoded_message)
    else:
        secret = decoded_message[3:-3]
        char = secret.pop()
        secret.insert(0, char)
        secret=''.join(secret)
    return secret