from string import ascii_lowercase as al

al_arr = list(al)
total = 26

def encode(plain_text):
    return calculated_text(plain_text)

def calculate_ciphered_index(index):
    return(total - int(index))

def calculated_text(text):
    ciphered_or_plain_text = ''
    for i,j in enumerate(text.lower()):
        indx = calculate_ciphered_index(int(al_arr.index(j)) + 1)
        ciphered_or_plain_text += al_arr[indx]
    return ciphered_or_plain_text

def decode(ciphered_text):
    return calculated_text(ciphered_text)

print(encode("OMG"))
