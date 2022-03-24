### OBJECTIVE
"""
Write a function which receives a list and returns the list reversed.
"""

### INPUT - DO NOT TOUCH
lst = eval(input())
### END INPUT

def reverser(lst):
    new_list = []
    for i in range(len(lst)-1, -1, -1):
        new_list.append(lst[i])
    return new_list


### OUTPUT - DO NOT TOUCH
print(reverser(lst))
### END OUTPUT


### EXAMPLE INPUT - YOU MAY COPY THIS INTO THE TERMINAL TO TEST YOUR CODE
### [1,2,3,4]

### EXAMPLE OUTPUT - YOU MAY UNCOMMENT THIS LINE TO CHECK THE EXAMPLE INPUT
# assert reverser(lst) == [4,3,2,1]