### OBJECTIVE
"""
You are given a string and it is you job to decrypt it. That's all you got, you are the expert, find out what to do ;)
"""

### INPUT - DO NOT TOUCH
original = eval(input())
### END INPUT

def encrypt(original):
    alphabet = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    decrypt = ''
    for i in original:
        if i == ' ':
            decrypt += ' '
        elif alphabet.index(i)+9 >= len(alphabet):
            decrypt += alphabet[alphabet.index(i) + 9-len(alphabet)]
        else:
            decrypt += alphabet[alphabet.index(i) + 9]

    return decrypt

### OUTPUT - DO NOT TOUCH
print(encrypt(original))
### END OUTPUT

### EXAMPLE INPUT - YOU MAY COPY THIS INTO THE TERMINAL TO TEST YOUR CODE
### FETV PFL BEFN KYV VETIPGKZFE RCXFIZKYD KYZJ NZCC SV IVRCCP VRJP KF UVTIPGKW SLK PFL NZCC EVMVI WZEU FLK DNRYRYRYRYR

### EXAMPLE OUTPUT - YOU MAY UNCOMMENT THIS LINE TO CHECK THE EXAMPLE INPUT
### assert caesar_encryption(original,shift) == "ONCE YOU KNOW THE ENCRYPTION ALGORITH THIS WILL BE REALLY EASY TO DECRYPT BUT YOU WILL NEVER FIND OUT MWAHAHAHAHA"