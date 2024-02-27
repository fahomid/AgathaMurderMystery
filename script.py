from constraint import *

# creating a CSP problem
problem = Problem()

# variables representing the people in the mansion
people = ['Agatha', 'Butler', 'Charles']

# variables for wealth (0: poorest, 1: richer, 2: richest)
problem.addVariables(people, [0, 1, 2])

# variables representing the killer and the victim
problem.addVariables(['the_killer', 'the_victim'], people)

# variables representing the hates and richer relations
for i in people:
    for j in people:
        problem.addVariables([f'{i}_hates_{j}', f'{i}_richer_{j}'], [0, 1])

# a killer always hates and is no richer than his victim
def killer_constraint(the_killer, the_victim, hates, richer):
    return hates == 1 and richer == 0

problem.addConstraint(killer_constraint, ('the_killer', 'the_victim', 'Agatha_hates_Butler', 'Agatha_richer_Butler'))

# concept of richer
def richer_constraint(i, j, richer):
    return (i == j and richer == 0) or (i != j and richer == 1)

# adding constraint for each pair of people
for i in people:
    for j in people:
        problem.addConstraint(richer_constraint, (i, j, f'{i}_richer_{j}'))

# charles hates no one that Agatha hates
def charles_constraint(charles, i, agatha_hates):
    return charles != i or agatha_hates == 0

problem.addConstraint(charles_constraint, ('Charles', 'Agatha', 'Agatha_hates_Charles'))

# agatha hates everybody except the butler
def agatha_constraint(agatha, i, butler_hates):
    return (agatha != i and butler_hates == 1) or (i == 'Butler' and agatha != i)

problem.addConstraint(agatha_constraint, ('Agatha', 'Charles', 'Butler_hates_Agatha'))

# Butler hates everyone not richer than Aunt Agatha
def butler_constraint(butler, i, richer):
    return butler != i or (butler == i and richer == 0)

for i in people:
    problem.addConstraint(butler_constraint, ('Butler', i, f'{i}_richer_Agatha'))

# Butler hates everyone whom Agatha hates
def butler_hate_constraint(butler, i, agatha_hates):
    return butler != i or (butler == i and agatha_hates == 1)

for i in people:
    problem.addConstraint(butler_hate_constraint, ('Butler', i, f'Agatha_hates_{i}'))

# no one hates everyone
def no_one_hates_everyone(*args):
    return sum(args) <= 2

for i in people:
    for j in people:
        if i != j:
            problem.addConstraint(no_one_hates_everyone, (f'{i}_hates_{j}', f'{j}_hates_{i}'))

# solving the CSP
solutions = problem.getSolutions()

# printing all the possible solutions
for solution in solutions:
    print("The killer:", solution['the_killer'])
    print("The victim:", solution['the_victim'])
    print("Hates:")
    for i in people:
        for j in people:
            print(solution[f'{i}_hates_{j}'], end=' ')
        print()
    print("Richer:")
    for i in people:
        for j in people:
            print(solution[f'{i}_richer_{j}'], end=' ')
        print()
    print()
