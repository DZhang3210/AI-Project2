from backtracking import parse_input, backtrack


def main():
    input_matrix, domain, one, double, degree = parse_input("inputs/Sample_Input.txt")
    print(input_matrix)
    print(domain)
    print(one)
    print(double)
    print(degree)

    res = backtrack(input_matrix, domain, one, double, degree)


if __name__ == "__main__":
    main()
