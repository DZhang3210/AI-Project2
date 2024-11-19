def next_value(domain, one, double, dup, valid_values):
    if not valid_values:
        return None
        
    min_mrv = float('inf')
    min_degree = float('-inf')
    min_current = None
    
    for (v_i, v_j) in valid_values:
        mrv = len(domain[(v_i, v_j)])
        degree = len(one[(v_i, v_j)]) + len(double[(v_i, v_j)]) + len(dup[(v_i, v_j)])
        
        if mrv < min_mrv or (mrv == min_mrv and degree > min_degree):
            min_mrv = mrv
            min_degree = degree
            min_current = (v_i, v_j)
            
    return min_current
