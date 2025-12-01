import re

# Link to challenge: https://adventofcode.com/2025/day/1


# Part 1
# def apply_operation(acum: int, operation: str) -> int:
# Part 2
def apply_operation(acum: int, operation: str) -> tuple[int, int]:
    """
    Apply the selected operation and return the resulting value
    PART2 (along with the value of k which corresponds to the
    times it "went past" 0)
    """

    regex_result = re.search(r"^([LR])(\d+)", operation)

    if not regex_result:
        raise ValueError(
            "Invalid operation. Expected L or R followed by a number, got " + operation
        )

    orientation, length = regex_result.groups()

    if orientation == "L":
        ret = acum - int(length)
    else:
        ret = acum + int(length)

    # PART 1
    # return ret % 100

    ## Part 2
    ## Modulus : result = ret % 100
    ## ret = k * 100 + result
    ## |k| = abs((ret - result) / 100)

    result = ret % 100
    # But we can use python's convenient interger division operator
    k = abs(ret // 100)

    # Finishing on 0 when going R will make us double count
    # Starting on 0 when going L will make us double count
    if (acum == 0 and ret < 0) or (result == 0 and ret >= 100):
        k -= 1

    return result, int(k)


def solve_puzzle(instructions: list[str]) -> int:
    """
    Solve the puzzle using the given instructions.
    """
    position = 50
    result = 0

    for instruction in instructions:
        position, num_zeros = apply_operation(position, instruction)

        result += abs(num_zeros)
        if position == 0:
            result += 1

    return result


fh = open("inputs/input_1.txt")
operations = []
for op in fh:
    operations.append(op.strip())

fh.close()

ret = solve_puzzle(operations)

print(ret)
