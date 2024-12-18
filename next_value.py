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
