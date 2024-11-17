from check_arcs import check_arcs
from next_value import next_value

#Recursive function that will backtrack through the matrix, trying to find a valid value for the current cell, if it fails, it will try the next value
def backtrack_step(domain, one, double, degree, valid_values):
    if len(valid_values) == 0:
        return matrix
    
    matrix = [[0 for _ in range(9)] for _ in range(9)]
    (i, j) = next_value(domain, one, double, valid_values)
    for value in domain[(i, j)]:
        res = check_arcs(matrix, domain, one, double, i, j, value)
        if res:
            matrix[i][j] = value
            valid_values.remove((i, j))
            value = backtrack_step(domain, one, double, degree, valid_values)
            if value:
                return value
            else:
                matrix[i][j] = 0
                valid_values.add((i, j))
    return None

    
           

