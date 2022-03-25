### OBJECTIVE
"""
Consider a clock:
A clock has 12 points on its circumference.
So n = 12 and let's say refNumber = 3 then we want to find the number opposite of the refNumber
In this case it should return 9. However, be cautious...
if n = 12 and refNumber = 10 the output should be 4.
"""

### INPUT - DO NOT TOUCH
n, refNumber = eval(input())
### END INPUT


def surround(n,refNumber):
    if refNumber <= n/2:
        return int(refNumber+n/2)
    else:
        return int(refNumber-n/2)

### OUTPUT - DO NOT TOUCH
print(surround(n,refNumber))
### END OUTPUT


### EXAMPLE INPUT - YOU MAY COPY THIS INTO THE TERMINAL TO TEST YOUR CODE
###10
###2

### EXAMPLE OUTPUT - YOU MAY UNCOMMENT THIS LINE TO CHECK THE EXAMPLE INPUT
###assert surround(n,refNumber) == 7