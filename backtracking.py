from check_arcs import check_arcs
from next_value import next_value
from copy import deepcopy


#Recursive function that will backtrack through the matrix, trying to find a valid value for the current cell, if it fails, it will try the next value
def backtrack_step(matrix, domain, one, double, dup, valid_values):
    if len(valid_values) == 0:
        print("No more valid values")
        # print(valid_values)
        return matrix
    
    (i, j) = next_value(domain, one, double, dup, valid_values)
    if (i, j) == None:
        return matrix
    # print("(i, j):")
    print((i, j))
    
    # print("Next Value:")
    # print((i, j))
    # print("Num Left:")
    # print(len(valid_values))
    valid_values.remove((i, j))
    print("Domain:")
    print(domain[(i, j)])
    for value in domain[(i, j)]:
      
        print("Value:")
        print(value)
        #Store a copy of the domain and the new domain after forward checking
        

        domain_copy = {k: list(v) for k, v in domain.items()}
        domain_copy = check_arcs(matrix, domain_copy, one, double, dup, i, j, value)
        #None or a new domain

        if domain_copy:
            
            # prev_domain = deepcopy(domain[(i, j)])
            
            #Store a copy of the domain before updating the domain

            matrix[i][j] = value
            domain_copy[(i, j)] = [value]
           
            result = backtrack_step(matrix, domain_copy, one, double, dup, valid_values)

            if result:
                print("Found result")
                return result
            
            matrix[i][j] = 0
            # domain[(i, j)] = prev_domain
            # domain = domain_copy
       
    valid_values.add((i, j))
    print("Ran out of values")
    return None

    
           

