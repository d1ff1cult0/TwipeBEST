"""
Find a sublist of the list that sums up to the given total
"""

### INPUT - DO NOT TOUCH ###
possibilities = list(map(int, input().split()))
total = int(input())
### END INPUT ###

def accountancy(possibilities, total):

    return list(min(subsom(total, possibilities)))

def extend(partial_solution, lijst):
    solutions = []
    for i in lijst:
        if lijst.count(i) > partial_solution.count(i):
            solutions.append(partial_solution + [i])
    return solutions

def examine(partial_solution, doelsom, lijst):
    if sum(partial_solution) == doelsom:
        return 'Accept'
    elif sum(partial_solution) < doelsom-min(lijst):
        return 'Continue'
    else:
        return 'Abandon'

def solve(doelsom, lijst, partial_solution):
    exam = examine(partial_solution, doelsom, lijst)
    if exam == 'Accept':
        return [partial_solution]
    elif exam != 'Abandon':
        solutions = []
        for p in extend(partial_solution, lijst):
            for i in solve(doelsom, lijst, p):
                if sorted(i) not in solutions:
                    solutions.append(sorted(i))
        return solutions
    return []

def subsom(doelsom, lijst, partial_solution=[]):
    solution = solve(doelsom, lijst, partial_solution)
    if not solution:
        return None
    else:
        new_sol = []
        for i in solution:
            new_sol.append(tuple(i))
        return new_sol

### OUTPUT - DO NOT TOUCH ###
answer = sorted(accountancy(possibilities, total), reverse=True) # Make 'answer' a list containing a (sorted) viable combination of values.
print(' '.join(map(str, answer)))
### END OUTPUT ###

### EXAMPLE INPUT - YOU MAY COPY THIS INTO YOUR TERMINAL
###58 180 350 94 220 52 106 202 545 79 32 33
###668

### EXAMPLE OUTPUT - UNCOMMENT THIS LINE TO CHECK YOUR CODE
### 545 58 33 32

