#Check consistency of one arcs, where if there is a 1-arc, the value must be one unit apart, it is assumed that matrix is will be assigned and unassigned outside this function

#you will return the domain, if it's consistent, and all neighbors still have valid values in their domain
def one_arc_consistency(matrix, one, i, j, value, domain):
    one_domain = one[(i, j)]
    for (v_i, v_j) in one_domain:       
        # For assigned cells
        if matrix[v_i][v_j] != 0:
            if abs(matrix[v_i][v_j] - value) != 1:
                return None
        # For unassigned cells
        else:
            # Keep only values that differ by exactly 1
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
            if smaller * 2 != larger:
                return None
        # For unassigned cells
        else:
            # Keep only values that satisfy the double relationship
            valid_values = [v for v in domain[(v_i, v_j)]
                          if max(v, value) == min(v, value) * 2]
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
def check_arcs(matrix, domain, one, double, dup, i, j, value):
    # Using deepcopy to create a completely independent copy of the domain dictionary
    # and all its nested structures (the lists of possible values)
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