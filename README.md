# AI-Project2

## Overview

For this project, I implemented a backtracking algorithm with forward checking for Kropki Sudoku Problem - I DID THE EXTRA CREDIT

## Instructions

In order to run the program, simply run the main.py file. If the main.py file is not in the same directory as the other files, you will need to adjust the file paths.

## Variables / Domains / Constraints

I had 6 inital values:
matrix is simple a 2d array representing the sudoku board
domain is a dictionary where the keys are the positions on the board and the values are the possible values for that position
one is a dictionary where the keys are the positions on the board and the values are a list of positions that are connected to the key by a one-arc
double is a dictionary where the keys are the positions on the board and the values are a list of positions that are connected to the key by a double-arc
dup is a dictionary where the keys are the positions on the board and the values are a list of positions that are connected to the key by a duplicate arc, which is essentially just the default sudoku constraints
valid_values is a list of positions on the board that have not been assigned a value yet, and is used mostly as a helper variable to check what I should use for the next value to assign

## Constraint Propagation

    In order to propagate the constraints, I created 3 helper functions:
        one_arc_consistency: checks if the value assigned to a position is consistent with the one-arcs
        double_arc_consistency: checks if the value assigned to a position is consistent with the double-arcs
        dup_arc_consistency: checks if the value assigned to a position is consistent with the duplicate arc

    each of these functions return either None, if the arc is inconsistent, or a new domain containing the values that are still valid for the position, for all related positions
        - these are tracked by the values: one, double, dup

    if the function returns None, then the domain is not updated, and the function will backtrack

    if the function returns a new domain, then the domain is updated, and the function will continue to check the next position
