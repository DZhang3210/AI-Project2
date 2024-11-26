from collections import defaultdict

def square_items(c_i, c_j):
    x = c_i//3
    y = c_j//3
    return [(i, j) for i in range(x*3, x*3+3) for j in range(y*3, y*3+3) if not (i == c_i and j == c_j)]
def row_items(c_i, c_j):
    return [(i, c_j) for i in range(9) if i != c_i]
def column_items(c_i, c_j):
    return [(c_i, j) for j in range(9) if j != c_j]


#Parse the input file and return the initial values, domain, one, double, and valid values
def parse_input(file_path):
    matrix = [[0 for _ in range(9)] for _ in range(9)]
    with open(file_path, 'r') as file:
        lines = file.readlines()
        initial_values = []
        domain = defaultdict(list)
        valid_values = set()

        # Parse initial 9x9 board
        for i, line in enumerate(lines[0:9]):
            # Strip whitespace and ensure we have 9 values
            values = list(map(int, line.strip().split()))
            if len(values) != 9:
                raise ValueError(f"Row {i} must contain exactly 9 values")
            
            for j, value in enumerate(values):
                if not 0 <= value <= 9:
                    raise ValueError(f"Invalid value {value} at position ({i},{j})")
                    
                if value != 0:
                    matrix[i][j] = value
                    domain[(i, j)].append(value)
                    initial_values.append(([i, j], value))
                else:
                    domain[(i, j)] = [1, 2, 3, 4, 5, 6, 7, 8, 9]
                    valid_values.add((i, j))

        
 
        one_arcs = defaultdict(list)
        double_arcs = defaultdict(list)
        dup_arcs = defaultdict(list)
        for i in range(9):
            for j in range(9):
                dup_arcs[(i, j)].extend(square_items(i, j))
                # print((i, j), "Square items:", dup_arcs[(i, j)])
                dup_arcs[(i, j)].extend(row_items(i, j))
                dup_arcs[(i, j)].extend(column_items(i, j))

        #Parse the for the arcs on horizontal axis
        for i, line in enumerate(lines[10:18]):
            values = list(map(int, line.strip().split()))
            if len(values) != 8:
                raise ValueError(f"Horizontal dots row {i} must contain exactly 8 values")
                
            for j, value in enumerate(values):
                if value not in [0, 1, 2]:
                    raise ValueError(f"Invalid dot value {value} at horizontal position ({i},{j})")
                if value == 1:
                    one_arcs[(i, j)].append((i,j+1))
                    one_arcs[(i, j+1)].append((i, j))
                elif value == 2:
                    double_arcs[(i, j)].append((i,j+1))
                    double_arcs[(i, j+1)].append((i, j))

        #Parse for arcs on the vertical axis
        for i, line in enumerate(lines[20:28]):  # Changed from lines[20:] to lines[20:28]
            values = list(map(int, line.strip().split()))
            if len(values) != 9:
                raise ValueError(f"Vertical dots row {i} must contain exactly 9 values")
                
            for j, value in enumerate(values):
                if value not in [0, 1, 2]:
                    raise ValueError(f"Invalid dot value {value} at vertical position ({i},{j})")
                if value == 1:
                    one_arcs[(i, j)].append((i+1, j))
                    one_arcs[(i+1, j)].append((i, j))
   
                elif value == 2:
                    double_arcs[(i, j)].append((i+1, j))
                    double_arcs[(i+1, j)].append((i, j))
           

    # Add input validation for empty file
    if not lines:
        raise ValueError("Input file is empty")

    # Validate total number of lines (should be at least 28 for a complete puzzle)
    if len(lines) < 28:
        raise ValueError("Input file is incomplete. Expected at least 28 lines")

    # Add documentation for return values
    """Returns:
        matrix: 9x9 grid of initial Sudoku values
        initial_values: List of ([i,j], value) tuples for filled cells
        domain: Dict of valid values for each cell
        one_arcs: Dict of coordinates connected by white dots (difference of 1)
        double_arcs: Dict of coordinates connected by black dots (difference of 2)
        dup_arcs: Dict of coordinates that can't have duplicate values
        valid_values: Set of coordinates that can be modified
    """
    return matrix, initial_values, domain, one_arcs, double_arcs, dup_arcs, valid_values

#Return values

#Initial values, we will store this to later insert in order to update arcs
#Domain, we will store the valid domain values of each cell
#One, Arcs where one coord is associated with a list of coords that are connected and whose value must be a diference of 1
    #We will store this as a list of tuples, where the first element is the coord and the second element is a list of coords that are connected and whose value must be a diference of 1
#Double, Arcs where one coord is associated with a list of coords that are connected and whose value must be a diference of 2
    #We will store this as a list of tuples, where the first element is the coord and the second element is a list of coords that are connected and whose value must be a diference of 2

#Valid values, coordinates of cells with initial values which we can choose from