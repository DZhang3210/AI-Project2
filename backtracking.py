from check_arcs import check_arcs
from next_value import next_value

#Recursive function that will backtrack through the matrix, trying to find a valid value for the current cell, if it fails, it will try the next value
def backtrack_step(matrix, domain, one, double, dup, valid_values):
    if len(valid_values) == 0:
        return matrix
    
    (i, j) = next_value(domain, one, double, dup, valid_values)
    print("Next Value:")
    print((i, j))
    for value in domain[(i, j)]:
        domain_copy = {k: list(v) for k, v in domain.items()}
        res = check_arcs(matrix, domain_copy, one, double, dup, i, j, value)
        if res:
            matrix[i][j] = value
            valid_values.remove((i, j))
            result = backtrack_step(matrix, domain_copy, one, double, dup, valid_values)
            if result:
                return result
            matrix[i][j] = 0
            valid_values.add((i, j))
    return None

    
           

