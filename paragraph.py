from encoder import encoder
from decoder import decoder

def encoder_paragraph(sentence):
    words = sentence.split()
    encoded_words=[]
    for word in words:
        encoded_words.append(encoder(word))
    new_sentence = ' '.join(encoded_words)
    return new_sentence

def decoder_paragraph(sentence):
    words = sentence.split()
    decoded_words=[]
    for word in words:
        decoded_words.append(decoder(word))
    new_sentence = ' '.join(decoded_words)
    return new_sentence