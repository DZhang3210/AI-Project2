from backtracking import  backtrack_step
from parse_input import parse_input



def main():
    matrix, initial_values, domain, one, double, dup, valid_values = parse_input("inputs/Sample_Input.txt")
    # print(double[(4,3)])
    # print(one[(4,3)])
    # matrix, initial_values, domain, one, double, dup, valid_values = parse_input("inputs/x1.txt")
    
    # Fill initial values
    # for (pos, value) in initial_values:
    #     matrix[pos[0]][pos[1]] = value

    # print("Matrix:")
    # print(matrix)

    # print("One:")
    # print(one)

 

    # print("Domain:")
    # print(domain)

    res = backtrack_step(matrix, domain, one, double, dup, 
    valid_values)

 
    print("Result:")
    print(res)


if __name__ == "__main__":
    main()
