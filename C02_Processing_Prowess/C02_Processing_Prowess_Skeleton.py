### OBJECTIVE
"""
Write a function which receives an integer n and returns the integer that the bits of n reversed
produce.

For example, 20 in binary is 10100. The output should be 5 since its binary representation is 00101.
"""

### INPUT - DO NOT TOUCH
n = int(input())
### END INPUT

def bit_reverser(n):
    binary = bin(n)[2:]
    binary = reversed(binary)
    new_binary = ""
    for i in binary:
        if i == '0':
            new_binary += '1'
        else:
            new_binary += '0'
    return int(new_binary, 2)

### OUTPUT - DO NOT TOUCH
print(bit_reverser(n))
### END OUTPUT


### EXAMPLE INPUT - YOU MAY COPY THIS INTO THE TERMINAL TO TEST YOUR CODE
### 20

### EXAMPLE OUTPUT - YOU MAY UNCOMMENT THIS LINE TO CHECK THE EXAMPLE INPUT
### assert bit_reverser(n) == 5