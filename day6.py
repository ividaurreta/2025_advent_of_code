
import re
import numpy as np
from functools import reduce

def apply_op(x: int, y: int, op: str) -> int:
    if op == '+':
        return x + y
    elif op == '*':
        return x * y
    else:
        raise ValueError(f"Invalid operator: {op}")

def solve_puzzle(matrix: np.array, operators: list) -> int:
    result = 0
    for i, row in enumerate(matrix): 
        op = operators[i]
        result += reduce(lambda x, y: apply_op(x, y, op), [int(x) for x in row])

    return result

def transform_row(row: list) -> list:
    resulting_row= []
    for number in row: 
        for i, char in enumerate(number):
            if i >= len(resulting_row):
                resulting_row.append(char)
            else:
                resulting_row[i] += char
    
    print(resulting_row)
    return resulting_row

        

def solve_puzzle_part2(matrix: list[str], operators: list) -> int:
    result = 0
    prev_operator = " "
    memory = []

    for i, op_elem in enumerate(operators):
        if op_elem in ['+', '*']:
            if prev_operator != " ":
                result += reduce(lambda x, y: apply_op(x, y, op), [int(x) for x in prev_operator])

            prev_operator = op_elem
            memory = []
        for row in matrix:
            for char in row:
                if i <= len(memory):
                    memory.append(char)
                else:
                    memory[i] += char


    return result

if __name__ == "__main__":
    fh = open("inputs/test_input.txt")
    matrix = []
    operators = []
    
    part_1 = False

    if part_1:
        for line in fh:
            processed_row = re.sub(r"\s{2,}", " ", line.strip()).split(" ")
            if processed_row[0] in ['+', '*']:
                operators = processed_row
            else:
                matrix.append(processed_row)

        matrix = np.array(matrix).transpose()

        sol1 = solve_puzzle(matrix, operators)
    else:
        for line in fh:
            row = line.strip()
            if row[0] in ['+', '*']:
                operators.append(row)
            else:
                # Matrix will be a list of strings instead of a list of lists
                matrix.append(row)

        sol2 = solve_puzzle_part2(matrix, operators)

    print("====================================")
    # print("Part 1 solution: ", sol1)
    print("Part 2 solution: ", sol2)
    print("====================================")
