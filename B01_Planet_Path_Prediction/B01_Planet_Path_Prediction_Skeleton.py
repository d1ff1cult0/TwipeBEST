### OBJECTIVE
"""
Write a function which receives two linear equations (which are represented by a tuple (a,b) for the equation y = ax + b)
and a third tuple which represents the range of x. Return a boolean that tells us if they the equations intersect within
this range.
"""

### INPUT - DO NOT TOUCH
eq1, eq2, rnge = eval(input())


### END INPUT


def linear_intersection(eq1, eq2, rnge):
    if eq1[0] == eq2[0] and eq1[1] == eq2[1]:
        return True
    elif eq1[0] == eq2[0]:
        return False

    if eq2[0] - eq1[0] != 0:
        x = (eq2[1] - eq1[1]) / (eq1[0] - eq2[0])
        if x and rnge[0] <= x <= rnge[1]:
            return True

    return False


### OUTPUT - DO NOT TOUCH
print(linear_intersection(eq1, eq2, rnge))
### END OUTPUT


### EXAMPLE INPUT - YOU MAY COPY THIS INTO THE TERMINAL TO TEST YOUR CODE
### ((3, -4), (-1, -5), (-4, 2))

### EXAMPLE OUTPUT - YOU MAY UNCOMMENT THIS LINE TO CHECK THE EXAMPLE INPUT
###assert linear_intersection(eq1, eq2, rnge) == True
