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

    
           

