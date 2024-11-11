from collections import defaultdict

#Parse the input file and return the initial values, domain, one, double, degree, and valid values
def parse_input(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        initial = []
        domain = defaultdict(list)
        valid_values = set()

        for i, line in enumerate(lines[0:9]):
           for j, value in enumerate(list(map(int, line.split()))):
               if value != 0:
                   domain[(i, j)].append(value)
                   initial.append(([i, j], value))
               else:
                   domain[(i, j)] = [1, 2, 3, 4, 5, 6, 7, 8, 9]
                   valid_values.add((i, j))
         
      
        degree = defaultdict(int)
        one = defaultdict(list)
        double = defaultdict(list)
        
        
        for i, line in enumerate(lines[10:18]):
            for j, value in enumerate(list(map(int, line.split()))):
                if value == 1:
                    one[(i, j)].append((i+1,j))
                    one[(i+1, j)].append((i, j))
                    degree[(i, j)] += 1
                    degree[(i+1, j)] += 1
                elif value == 2:
                    double[(i, j)].append((i+1,j))
                    double[(i+1, j)].append((i, j))
                    degree[(i, j)] += 1
                    degree[(i+1, j)] += 1

        for i, line in enumerate(lines[20:]):
            for j, value in enumerate(list(map(int, line.split()))):
                if value == 1:
                    one[(i, j)].append((i, j+1))
                    one[(i, j+1)].append((i, j))
                    degree[(i, j)] += 1
                    degree[(i, j+1)] += 1
                elif value == 2:
                    double[(i, j)].append((i, j+1))
                    double[(i, j+1)].append((i, j))
                    degree[(i, j)] += 1
                    degree[(i, j+1)] += 1

    return initial, domain, one, double, degree, valid_values

#Give order of domain values to try for a cell
#We assume that forward checking is already done and that all values in the domain are valid
def order_domain_values(matrix, domain, valid_values, i, j):
    if (i, j) in valid_values:
        return []
    domain_values = domain[(i, j)]
    domain_values.sort()
    return domain_values

#Get the square items of a cell
def square_items(c_i, c_j):
    x = c_i//3
    y = c_j//3
    return [(i, j) for i in range(x, x+3) for j in range(y, y+3) if (i != c_i and j != c_j)]

def square_consistent(matrix, domain, i, j, value):
    variables = square_items(i, j)
    items = set()
    for (v_i, v_j) in variables:
        if v_i == i and v_j == j: continue
        if matrix[v_i][v_j] != 0: items.add(matrix[v_i][v_j])
        else:
            domain[(v_i, v_j)].remove(value)
        if value in items:
            return False
    return True

def side_consistent(matrix, domain, i, j, value):
    row = [(i, v_j) for v_j in range(9) if v_j != j]
    items = set()
    for (v_i, v_j) in row:
        if v_i == i and v_j == j: continue
        if matrix[v_i][v_j] != 0: items.add(matrix[v_i][v_j])
        else:
            domain[(v_i, v_j)].remove(value)
            if len(domain[(v_i, v_j)]) == 0:
                return False
        if value in items:
            return False
    
    column = [(v_i, j) for v_i in range(9) if v_i != i]
    items = set()
    for (v_i, v_j) in column:
        if v_i == i and v_j == j: continue
        if matrix[v_i][v_j] != 0: items.add(matrix[v_i][v_j])
        else:
            domain[(v_i, v_j)].remove(value)
            if len(domain[(v_i, v_j)]) == 0:
                return False
        if value in items:
            return False
    return True

#Check consistency of arcs, where if there is a 1-arc, the value must be one unit apart, and if there is a 2-arc, the value must be two units apart
def check_arcs(matrix, domain, one, double, i, j, value):
    one_domain = one[(i, j)]
    for (v_i, v_j) in one_domain:       
        if matrix[v_i][v_j] != 0:
            diff = abs(matrix[v_i][v_j] - value)
            if diff != 1:
                return False
        else:
            for domain_value in domain[(v_i, v_j)]:
                if abs(domain_value - value) == 1:
                    continue
                else:
                    domain[(v_i, v_j)].remove(domain_value)
                    if len(domain[(v_i, v_j)]) == 0:
                        return False
            
    double_domain = double[(i, j)]
    for (v_i, v_j) in double_domain:       
        if matrix[v_i][v_j] != 0:
            (x1, x2) = max(matrix[v_i][v_j], value), min(matrix[v_i][v_j], value)
            if x2*2 != x1:
                return False
        else:
            for domain_value in domain[(v_i, v_j)]:
                if domain_value == value*2 or (domain_value%2 == 0 and domain_value//2 == value):
                    continue
                else:
                    domain[(v_i, v_j)].remove(domain_value)
                    if len(domain[(v_i, v_j)]) == 0:
                        return False
    return True    

#Check consistency of a cell, where the value must be consistent with the square, side, and arc neighbors
def check_consistency(matrix, domain, one, double, i, j, value):
    return square_consistent(matrix, domain, i, j, value) and side_consistent(matrix, domain, i, j, value) and check_arcs(matrix, domain, one, double, i, j, value)

#Populate the matrix with the domain values, checking consistency at each step
def populate_matrix(matrix, domain, one, double, i, j):
    if (i == None or j == None):
        i, j = 0, 0
    for value in domain[(i, j)]:
        current_domain = domain.copy()
        res = check_consistency(matrix, domain, one, double, i, j, value)
        if res:
            matrix[i][j] = value
            populate_matrix(matrix, domain, one, double, i, j)
            domain = current_domain
            matrix[i][j] = 0
        else:
            domain = current_domain

    



def backtrack(initial, domain, one, double, degree, valid_values):
    matrix = [[0 for _ in range(9)] for _ in range(9)]

    for (i, j), value in initial:
        res = check_consistency(matrix, domain, one, double, i, j, value)
        if res:
            matrix[i][j] = value
        else:
            return None

    populate_matrix(matrix, domain, one, double, None, None)

    return matrix

    
           

