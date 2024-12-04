# AI-Project2

## Overview

For this project, I implemented a backtracking algorithm with forward checking for Kropki Sudoku Problem - I DID THE EXTRA CREDIT

## Instructions

In order to run the program, simply run the main.py file. If the main.py file is not in the same directory as the other .py files, you will need to adjust the file paths. If you want to run the program with a different input or output file, you can change the file paths in the main.py file.

## Kropki Sudoku as a Constraint Satisfaction Problem

### Variables and Domains

Variables: Each cell in the 9x9 Sudoku grid, represented as positions in a 2D array (matrix)
Domains: A dictionary mapping each cell position to its set of possible values (1-9)

Initial domains are constrained by the given values in the puzzle
Each key is a cell position, and the domain is the set of possible numbers for that cell

### Constraints

#### Standard Sudoku Constraints (Duplicate Arcs):

Each row must contain numbers 1-9 without repetition
Each column must contain numbers 1-9 without repetition
Each 3x3 box must contain numbers 1-9 without repetition
Stored in dup dictionary: {position: [list of positions that cannot share the same value]}

#### Kropki Dots Constraints:

**One-Dot (White) Constraints:**
Adjacent numbers must differ by exactly 1
Stored in one dictionary: {position: [list of positions connected by white dots]}

**Two-Dot (Black) Constraints:**
One number must be exactly double the other
Stored in double dictionary: {position: [list of positions connected by black dots]}

### Helper Data Structures

**valid_values:** List of unassigned positions on the board
**matrix:** 2D array representing the current state of the Sudoku board

### Constraint Propagation

The solution implements three main constraint checking functions:

**one_arc_consistency(position, value):**

Verifies if assigning a value satisfies all white dot constraints
Returns updated domain if consistent, None if inconsistent

**double_arc_consistency(position, value):**

Verifies if assigning a value satisfies all black dot constraints
Returns updated domain if consistent, None if inconsistent

**dup_arc_consistency(position, value):**

Verifies if assigning a value satisfies standard Sudoku constraints
Returns updated domain if consistent, None if inconsistent

**For each constraint check:**

- If inconsistent (returns None): Backtrack to previous state
- If consistent: Update domains and continue with next position
- Domain updates propagate to affected neighboring cells

## Source Code

### Parse-Input.py

from collections import defaultdict

def square_items(c_i, c_j):
x = c_i//3
y = c_j//3
return [(i, j) for i in range(x*3, x*3+3) for j in range(y*3, y*3+3) if not (i == c_i and j == c_j)]
def row_items(c_i, c_j):
return [(i, c_j) for i in range(9) if i != c_i]
def column_items(c_i, c_j):
return [(c_i, j) for j in range(9) if j != c_j]

#Parse the input file and return the initial values, domain, one, double, and valid values
def parse*input(file_path):
matrix = [[0 for * in range(9)] for \_ in range(9)]
with open(file_path, 'r') as file:
lines = file.readlines()
domain = defaultdict(list)
valid_values = set()

        # Parse initial 9x9 board
        for i, line in enumerate(lines[0:9]):
            # Strip whitespace and ensure we have 9 values
            values = list(map(int, line.strip().split()))
            if len(values) != 9:
                raise ValueError(f"Row {i} must contain exactly 9 values")

            for j, value in enumerate(values):
                if not 0 <= value <= 9:
                    raise ValueError(f"Invalid value {value} at position ({i},{j})")

                if value != 0:
                    matrix[i][j] = value
                    domain[(i, j)].append(value)
                else:
                    domain[(i, j)] = [1, 2, 3, 4, 5, 6, 7, 8, 9]
                    valid_values.add((i, j))



        one_arcs = defaultdict(list)
        double_arcs = defaultdict(list)
        dup_arcs = defaultdict(list)
        for i in range(9):
            for j in range(9):
                dup_arcs[(i, j)].extend(square_items(i, j))
                dup_arcs[(i, j)].extend(row_items(i, j))
                dup_arcs[(i, j)].extend(column_items(i, j))

        #Parse the for the arcs on horizontal axis
        for i, line in enumerate(lines[10:18]):
            values = list(map(int, line.strip().split()))
            if len(values) != 8:
                raise ValueError(f"Horizontal dots row {i} must contain exactly 8 values")

            for j, value in enumerate(values):
                if value not in [0, 1, 2]:
                    raise ValueError(f"Invalid dot value {value} at horizontal position ({i},{j})")
                if value == 1:
                    one_arcs[(i, j)].append((i,j+1))
                    one_arcs[(i, j+1)].append((i, j))
                elif value == 2:
                    double_arcs[(i, j)].append((i,j+1))
                    double_arcs[(i, j+1)].append((i, j))

        #Parse for arcs on the vertical axis
        for i, line in enumerate(lines[20:28]):  # Changed from lines[20:] to lines[20:28]
            values = list(map(int, line.strip().split()))
            if len(values) != 9:
                raise ValueError(f"Vertical dots row {i} must contain exactly 9 values")

            for j, value in enumerate(values):
                if value not in [0, 1, 2]:
                    raise ValueError(f"Invalid dot value {value} at vertical position ({i},{j})")
                if value == 1:
                    one_arcs[(i, j)].append((i+1, j))
                    one_arcs[(i+1, j)].append((i, j))

                elif value == 2:
                    double_arcs[(i, j)].append((i+1, j))
                    double_arcs[(i+1, j)].append((i, j))


    # Add input validation for empty file
    if not lines:
        raise ValueError("Input file is empty")

    # Validate total number of lines (should be at least 28 for a complete puzzle)
    if len(lines) < 28:
        raise ValueError("Input file is incomplete. Expected at least 28 lines")

    # Add documentation for return values
    """Returns:
        matrix: 9x9 grid of initial Sudoku values
        initial_values: List of ([i,j], value) tuples for filled cells
        domain: Dict of valid values for each cell
        one_arcs: Dict of coordinates connected by white dots (difference of 1)
        double_arcs: Dict of coordinates connected by black dots (difference of 2)
        dup_arcs: Dict of coordinates that can't have duplicate values
        valid_values: Set of coordinates that can be modified
    """
    return matrix, domain, one_arcs, double_arcs, dup_arcs, valid_values

#Return values

#Initial values, we will store this to later insert in order to update arcs
#Domain, we will store the valid domain values of each cell
#One, Arcs where one coord is associated with a list of coords that are connected and whose value must be a diference of 1
#We will store this as a list of tuples, where the first element is the coord and the second element is a list of coords that are connected and whose value must be a diference of 1
#Double, Arcs where one coord is associated with a list of coords that are connected and whose value must be a diference of 2
#We will store this as a list of tuples, where the first element is the coord and the second element is a list of coords that are connected and whose value must be a diference of 2

#Valid values, coordinates of cells with initial values which we can choose from

### next_value.py

#using mrv and degree as well as valid_values, we will return the next value to be assigned
def next_value(domain, one, double, dup, valid_values):
if not valid_values:
return None

    min_mrv = float('inf')
    max_degree = float('-inf')
    min_current = None

    #iterate through all the valid values
    for (v_i, v_j) in valid_values:
        #calculate mrv
        mrv = len(domain[(v_i, v_j)])
        #calculate degree
        degree = len(one[(v_i, v_j)]) + len(double[(v_i, v_j)]) + len(dup[(v_i, v_j)])

        #if mrv is less than the minimum mrv or if mrv is equal to the minimum mrv and degree is greater than the maximum degree, we update the minimum mrv and maximum degree and the current minimum
        if mrv < min_mrv or (mrv == min_mrv and degree > max_degree):
            min_mrv = mrv
            max_degree = degree
            min_current = (v_i, v_j)

    return min_current

### check_arcs.py

#Check consistency of one arcs, where if there is a 1-arc, the value must be one unit apart, it is assumed that matrix is will be assigned and unassigned outside this function

#you will return the domain, if it's consistent, and all neighbors still have valid values in their domain
def one_arc_consistency(matrix, one, i, j, value, domain):
one_domain = one[(i, j)]
for (v_i, v_j) in one_domain:

# For assigned cells

if matrix[v_i][v_j] != 0:
if abs(matrix[v_i][v_j] - value) != 1:
return None # For unassigned cells
else: # Keep only values that differ by exactly 1
valid_values = [v for v in domain[(v_i, v_j)]
if abs(v - value) == 1]
if not valid_values:
return None

            domain[(v_i, v_j)] = valid_values
    return domain

def double_arc_consistency(matrix, double, i, j, value, domain):
double_domain = double[(i, j)]
for (v_i, v_j) in double_domain:

# For assigned cells

if matrix[v_i][v_j] != 0:
larger, smaller = max(matrix[v_i][v_j], value), min(matrix[v_i][v_j], value)
if smaller _ 2 != larger:
return None # For unassigned cells
else: # Keep only values that satisfy the double relationship
valid_values = [v for v in domain[(v_i, v_j)]
if max(v, value) == min(v, value) _ 2]
if not valid_values:
return None

            domain[(v_i, v_j)] = valid_values
    return domain

def dup_arc_consistency(matrix, dup, i, j, value, domain):
dup_domain = dup[(i, j)]
for (v_i, v_j) in dup_domain:
if matrix[v_i][v_j] != 0:
if matrix[v_i][v_j] == value:
return None
else:
if value in domain[(v_i, v_j)]:
domain[(v_i, v_j)].remove(value)
if len(domain[(v_i, v_j)]) == 0:
return None
return domain

from copy import deepcopy

#If it checks both one_arc_consistency and double_arc_consistency, if any of them returns None, it means that the domain is not consistent, and you should return None, which means to not update the domain, and instead try a new value
def check_arcs(matrix, domain, one, double, dup, i, j, value): # Using deepcopy to create a completely independent copy of the domain dictionary # and all its nested structures (the lists of possible values)
copy_domain = deepcopy(domain)
copy_domain = one_arc_consistency(matrix, one, i, j, value, copy_domain)
if copy_domain == None:
return None
copy_domain = double_arc_consistency(matrix, double, i, j, value, copy_domain)
if copy_domain == None:
return None
copy_domain = dup_arc_consistency(matrix, dup, i, j, value, copy_domain)
if copy_domain == None:
return None
return copy_domain

### backtracking.py

from check_arcs import check_arcs
from next_value import next_value
from copy import deepcopy

#Recursive function that will backtrack through the matrix, trying to find a valid value for the current cell, if it fails, it will try the next value
def backtrack_step(matrix, domain, one, double, dup, valid_values):
if len(valid_values) == 0:
return matrix

    #Get the next value to be assigned
    (i, j) = next_value(domain, one, double, dup, valid_values)
    if (i, j) == None:
        return matrix

    #Remove the coordinate from the valid values
    valid_values.remove((i, j))

    #Iterate through all the valid values for the current cell
    for value in domain[(i, j)]:
        #Store a copy of the domain and the new domain after forward checking
        domain_copy = {k: list(v) for k, v in domain.items()}
        domain_copy = check_arcs(matrix, domain_copy, one, double, dup, i, j, value)

        if domain_copy:
            #Assign the value to the current cell
            matrix[i][j] = value
            #Update the domain of the current cell
            domain_copy[(i, j)] = [value]

            result = backtrack_step(matrix, domain_copy, one, double, dup, valid_values)

            if result:
                return result

            #If the result is None, we need to backtrack, so we reset the value of the current cell to 0
            matrix[i][j] = 0

    #Add the coordinate back to the valid values
    valid_values.add((i, j))
    return None

### main.py

from backtracking import backtrack_step
from parse_input import parse_input

#matrix = 9x9 matrix with inital values
#domain = dictionary with coordinates as keys and list of valid values as values
#one = dictionary with coordinates as keys and list of coordinates connected by white dots as values
#double = dictionary with coordinates as keys and list of coordinates connected by black dots as values
#dup = dictionary with coordinates as keys and list of coordinates that can't have duplicate values as values
#valid_values = set of coordinates that can be modified

def main():
matrix, domain, one, double, dup, valid_values = parse_input("inputs/input3.txt")

    res = backtrack_step(matrix, domain, one, double, dup,
    valid_values)

    print("Result:")
    print(res)

    # Write result to output file
    if res:
        with open("outputs/output3.txt", "w") as f:
            for i in range(9):
                row = " ".join(str(res[i][j]) for j in range(9))
                f.write(row + "\n")

if **name** == "**main**":
main()

## Output 1

9 8 1 5 6 2 7 3 4
2 5 4 3 7 9 1 8 6
7 6 3 1 4 8 9 5 2
1 7 5 9 2 4 3 6 8
8 2 9 6 1 3 5 4 7
3 4 6 8 5 7 2 9 1
4 1 8 7 3 5 6 2 9
6 3 2 4 9 1 8 7 5
5 9 7 2 8 6 4 1 3

## Output 2

6 2 4 1 9 3 8 5 7
1 7 3 5 6 8 4 2 9
9 5 8 4 7 2 3 1 6
4 3 5 7 2 6 9 8 1
8 1 7 9 3 4 2 6 5
2 9 6 8 5 1 7 3 4
7 4 2 6 8 5 1 9 3
3 6 1 2 4 9 5 7 8
5 8 9 3 1 7 6 4 2

## Output 3

7 3 6 1 2 9 4 5 8
2 1 5 6 8 4 3 9 7
9 8 4 7 5 3 2 6 1
5 4 8 3 6 2 1 7 9
6 2 1 9 7 8 5 3 4
3 9 7 4 1 5 6 8 2
8 6 9 5 4 1 7 2 3
1 7 2 8 3 6 9 4 5
4 5 3 2 9 7 8 1 6
