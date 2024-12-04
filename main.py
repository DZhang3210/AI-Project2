from backtracking import  backtrack_step
from parse_input import parse_input


#matrix = 9x9 matrix with inital values
#domain = dictionary with coordinates as keys and list of valid values as values
#one = dictionary with coordinates as keys and list of coordinates connected by white dots as values
#double = dictionary with coordinates as keys and list of coordinates connected by black dots as values
#dup = dictionary with coordinates as keys and list of coordinates that can't have duplicate values as values
#valid_values = set of coordinates that can be modified

def main():
    matrix, domain, one, double, dup, valid_values = parse_input("inputs/input3.txt")

    res = backtrack_step(matrix, domain, one, double, dup, 
    valid_values)

    print("Result:")
    print(res)
    
    # Write result to output file
    if res:
        with open("Outputs/output3.txt", "w") as f:
            for i in range(9):
                row = " ".join(str(res[i][j]) for j in range(9))
                f.write(row + "\n")


if __name__ == "__main__":
    main()
