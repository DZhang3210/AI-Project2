#Check consistency of one arcs, where if there is a 1-arc, the value must be one unit apart, it is assumed that matrix is will be assigned and unassigned outside this function

#you will return the domain, if it's consistent, and all neighbors still have valid values in their domain
def one_arc_consistency(matrix,one, i, j, value, domain):
    one_domain = one[(i, j)]
    for (v_i, v_j) in one_domain:       
        #If the cell is already assigned, check if the value is consistent with the arc
        if matrix[v_i][v_j] != 0:
            diff = abs(matrix[v_i][v_j] - value)
            if diff != 1:
                return None
        #If the cell is not assigned, remove the values from the domain that are not consistent with the arc
        else:
            for domain_value in domain[(v_i, v_j)]:
                if abs(domain_value - value) == 1:
                    continue
                else:
                    domain[(v_i, v_j)].remove(domain_value)
            if len(domain[(v_i, v_j)]) == 0:
                return None
    return domain

def double_arc_consistency(matrix, double, i, j, value, domain):
    double_domain = double[(i, j)]
    for (v_i, v_j) in double_domain:       
        if matrix[v_i][v_j] != 0:
            (x1, x2) = max(matrix[v_i][v_j], value), min(matrix[v_i][v_j], value)
            if x2*2 != x1:
                return None
        else:
            for domain_value in domain[(v_i, v_j)]:
                if domain_value == value*2 or (domain_value%2 == 0 and domain_value//2 == value):
                    continue
                else:
                    domain[(v_i, v_j)].remove(domain_value)
                    if len(domain[(v_i, v_j)]) == 0:
                        return None
    return domain

def dup_arc_consistency(matrix, dup, i, j, value, domain):
    dup_domain = dup[(i, j)]
    for (v_i, v_j) in dup_domain:
        if matrix[v_i][v_j] != 0 and matrix[v_i][v_j] == value:
            return False
        else:
            for domain_value in domain[(v_i, v_j)]:
                if domain_value == value:
                    domain[(v_i, v_j)].remove(domain_value)
            if len(domain[(v_i, v_j)]) == 0:
                return False
    return True


#If it checks both one_arc_consistency and double_arc_consistency, if any of them returns None, it means that the domain is not consistent, and you should return None, which means to not update the domain, and instead try a new value
def check_arcs(matrix, domain, one, double, dup, i, j, value):
    domain = one_arc_consistency(matrix, one, i, j, value, domain)
    if domain == None:
        return None
    domain = double_arc_consistency(matrix, double, i, j, value, domain)
    if domain == None:
        return None
    domain = dup_arc_consistency(matrix, dup, i, j, value, domain)
    if domain == False:
        return None
    return domain    