def is_silly_number(number: str) -> bool:
    """
    Determine if the given number is silly.
    """
    # Don't really need to do integer division since it will always be even
    # because I discard uneven numbers but still keeping it for casting purposes
    half_point = len(number) // 2

    return number[:half_point] == number[half_point:]


def is_silly_number_with_queues(number: str) -> bool:
    """
    Similar to is_silly_number but now the number can be repeated multiple times
    So, we keep two queues:
    | 2 |
    | 1 | ==> Queue 1: Contains the number we believe is getting repeated
    |_1_|

    | 2 |
    |.1 | ==> Queue 2: Contains the repetitions and updates Queue1 if necessary
    |_1_|
    """

    queue_1: list[str] = []
    i_q1 = 0
    queue_2: list[str] = []
    i_q2 = 0

    for digit in number:
        len_q1 = len(queue_1)
        if len_q1 == 0:
            queue_1.append(digit)
        elif digit == queue_1[i_q1 % len_q1]:
            queue_2.append(digit)
            i_q1 += 1
        else:
            queue_2.append(digit)
            queue_1 = queue_1 + queue_2
            queue_2 = []
            i_q1 = 0

    # Fails if the whole number is in queue_1
    return len(queue_1) <= len(queue_2)


def solve_puzzle_part1(ranges: list[str]) -> int:
    acum = 0
    for r in ranges:
        start, end = r.split("-")
        if len(str(start)) % 2 != 0 and len(str(end)) % 2 != 0:
            # Numbers with odd length are not silly
            continue
        for i in range(int(start), int(end) + 1):
            if is_silly_number(str(i)):
                acum += i

    print("Total: " + str(acum))

    return acum


def solve_puzzle_part2(ranges: list[str]) -> int:
    acum = 0
    for r in ranges:
        start, end = r.split("-")
        for i in range(int(start), int(end) + 1):
            if is_silly_number_with_queues(str(i)):
                acum += i

    print("Total: " + str(acum))

    return acum


if __name__ == "__main__":

    # fh = open("inputs/input_2.txt")

    # all_ranges: str = fh.readline()

    # ranges: list[str] = all_ranges.split(",")

    # solve_puzzle_part2(ranges)

    # fh.close()

    print(is_silly_number_with_queues("1188511885"))
