from backtracking import  backtrack_step
from parse_input import parse_input


def main():
    initial_values, domain, one, double, dup, valid_values = parse_input("inputs/Sample_Input.txt")
    matrix = [[0 for _ in range(9)] for _ in range(9)]
    
    # Fill initial values
    # for (pos, value) in initial_values:
    #     matrix[pos[0]][pos[1]] = value
    
    print("One:")
    print(one)

    res = backtrack_step(matrix, domain, one, double, dup, valid_values)
    print("Result:")
    print(res)


if __name__ == "__main__":
    main()
