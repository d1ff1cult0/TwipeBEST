### OBJECTIVE
"""
Write a function which receives two linear equations (which are represented by a tuple (a,b) for the equation y = ax + b)
and a third tuple which represents the range of x. Return a boolean that tells us if they the equations intersect within
this range.
"""

### INPUT - DO NOT TOUCH
eq1, eq2, rnge = eval(input())
### END INPUT


def linear_intersection(eq1: tuple[int], eq2: tuple[int], rnge: tuple[int]) -> bool:
    # TODO
    pass

### OUTPUT - DO NOT TOUCH
print(linear_intersection(eq1, eq2))
### END OUTPUT


### EXAMPLE INPUT - YOU MAY COPY THIS INTO THE TERMINAL TO TEST YOUR CODE
### ((3, -4), (-1, -5), (-4, 2))

### EXAMPLE OUTPUT - YOU MAY UNCOMMENT THIS LINE TO CHECK THE EXAMPLE INPUT
### assert linear_intersection(eq1, eq2, rnge) == True