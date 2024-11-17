from collections import defaultdict

def square_items(c_i, c_j):
    x = c_i//3
    y = c_j//3
    return [(i, j) for i in range(x, x+3) for j in range(y, y+3) if (i != c_i and j != c_j)]
def row_items(c_i, c_j):
    return [(i, c_j) for i in range(9) if i != c_i]
def column_items(c_i, c_j):
    return [(c_i, j) for j in range(9) if j != c_j]


#Parse the input file and return the initial values, domain, one, double, degree, and valid values
def parse_input(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        initial_values = []
        domain = defaultdict(list)
        valid_values = set()

        for i, line in enumerate(lines[0:9]):
           for j, value in enumerate(list(map(int, line.split()))):
               if value != 0:
                   domain[(i, j)].append(value)
                   initial_values.append(([i, j], value))
               else:
                   domain[(i, j)] = [1, 2, 3, 4, 5, 6, 7, 8, 9]
                   valid_values.add((i, j))
         
      
        degree = defaultdict(int)
        one_arcs = defaultdict(list)
        double_arcs = defaultdict(list)
        dup_arcs = defaultdict(list)
        for i in range(9):
            for j in range(9):
                dup_arcs[(i, j)].extend(square_items(i, j))
                dup_arcs[(i, j)].extend(row_items(i))
                dup_arcs[(i, j)].extend(column_items(j))
        #Parse the for the arcs on horizontal axis
        for i, line in enumerate(lines[10:18]):
            for j, value in enumerate(list(map(int, line.split()))):
                if value == 1:
                    one_arcs[(i, j)].append((i+1,j))
                    one_arcs[(i+1, j)].append((i, j))
                    degree[(i, j)] += 1
                    degree[(i+1, j)] += 1
                elif value == 2:
                    double_arcs[(i, j)].append((i+1,j))
                    double_arcs[(i+1, j)].append((i, j))
                    degree[(i, j)] += 1
                    degree[(i+1, j)] += 1

        #Parse for arcs on the vertical axis
        for i, line in enumerate(lines[20:]):
            for j, value in enumerate(list(map(int, line.split()))):
                if value == 1:
                    one_arcs[(i, j)].append((i, j+1))
                    one_arcs[(i, j+1)].append((i, j))
                    degree[(i, j)] += 1
                    degree[(i, j+1)] += 1
                elif value == 2:
                    double_arcs[(i, j)].append((i, j+1))
                    double_arcs[(i, j+1)].append((i, j))
                    degree[(i, j)] += 1
                    degree[(i, j+1)] += 1

    return initial_values, domain, one_arcs, double_arcs, dup_arcs, degree, valid_values

#Return values

#Initial values, we will store this to later insert in order to update arcs
#Domain, we will store the valid domain values of each cell
#One, Arcs where one coord is associated with a list of coords that are connected and whose value must be a diference of 1
    #We will store this as a list of tuples, where the first element is the coord and the second element is a list of coords that are connected and whose value must be a diference of 1
#Double, Arcs where one coord is associated with a list of coords that are connected and whose value must be a diference of 2
    #We will store this as a list of tuples, where the first element is the coord and the second element is a list of coords that are connected and whose value must be a diference of 2

#Degree, the number of current unassigned neighbors of a cell

#Valid values, coordinates of cells with initial values which we can choose from