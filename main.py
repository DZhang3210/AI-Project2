from backtracking import  backtrack_step
from parse_input import parse_input



def main():
    matrix, initial_values, domain, one, double, dup, valid_values = parse_input("inputs/Sample_Input.txt")

    res = backtrack_step(matrix, domain, one, double, dup, 
    valid_values)

    print("Result:")
    print(res)
    
    # Write result to output file
    if res:
        with open("outputs/output.txt", "w") as f:
            for i in range(9):
                row = " ".join(str(res[i][j]) for j in range(9))
                f.write(row + "\n")


if __name__ == "__main__":
    main()
