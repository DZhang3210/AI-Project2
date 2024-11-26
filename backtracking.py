from check_arcs import check_arcs
from next_value import next_value
from copy import deepcopy


#Recursive function that will backtrack through the matrix, trying to find a valid value for the current cell, if it fails, it will try the next value
def backtrack_step(matrix, domain, one, double, dup, valid_values):
    if len(valid_values) == 0:
        return matrix
    
    (i, j) = next_value(domain, one, double, dup, valid_values)
    if (i, j) == None:
        return matrix

    valid_values.remove((i, j))
    for value in domain[(i, j)]:
        #Store a copy of the domain and the new domain after forward checking
        domain_copy = {k: list(v) for k, v in domain.items()}
        domain_copy = check_arcs(matrix, domain_copy, one, double, dup, i, j, value)

        if domain_copy:
            #Store a copy of the domain before updating the domain

            matrix[i][j] = value
            domain_copy[(i, j)] = [value]
           
            result = backtrack_step(matrix, domain_copy, one, double, dup, valid_values)

            if result:
                return result
            
            matrix[i][j] = 0
       
    valid_values.add((i, j))
    return None

    
           

