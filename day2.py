import re


def is_silly_number(number: str) -> bool:
    """
    Determine if the given number is silly where X = YY

    I already removed all odd length numbers because they can never
    be silly. After that, checking if a number is silly is just a
    matter of looking for the half point and comparing both halves.
    """
    half_point = len(number) // 2

    return number[:half_point] == number[half_point:]


def is_silly_number_with_incremental_multiplier(number: str) -> bool:
    """
    For any string of length X, if it's a silly number, meaning that it has
    a sequence of numbers repeated _at least_ twice, then it will be at the
    repeated number will have at most length X/2.

    Knowing that, because i'm dumb as rocks we will just brute force checking
    all substrings until we find the adequate substring or we run out of options

    """

    index = 1

    while index <= len(number) // 2:
        elem = number[:index]
        if (len(number) % index) == 0:
            multiplier = len(number) // index
            if elem * multiplier == number:
                return True

        index += 1

    return False


def is_silly_number_with_regex(number: str, part1: bool) -> bool:
    """
    Feels like cheating, but i freaking love RegEx
    Run it on https://regexr.com/ for a better explanation:

    ^ => Start of line
    (\\d+) => Group Match, a number with 1 or more digits. (Note: I'm escaping the escape bc it throws a warning if not for some reason)
    \1+    => The same group match we got gets repeated one or more time (we remove the + on part 1 for obvious reasons)
    $ => end of line
    """
    if part1:
        return re.match(r"^(\d+)\1$", number)

    return re.match(r"^(\d+)\1+$", number)


def solve_puzzle_part1(ranges: list[str]) -> int:
    acum = 0
    for r in ranges:
        start, end = r.split("-")
        if len(str(start)) % 2 != 0 and len(str(end)) % 2 != 0:
            # Numbers with odd length are not silly
            continue
        for i in range(int(start), int(end) + 1):
            if is_silly_number_with_regex(str(i), True):
                acum += i

    return acum


def solve_puzzle_part2(ranges: list[str]) -> int:
    acum = 0
    for r in ranges:
        start, end = r.split("-")
        for i in range(int(start), int(end) + 1):
            if is_silly_number_with_regex(str(i), False):
                acum += i

    return acum


if __name__ == "__main__":

    fh = open("inputs/input_2.txt")

    all_ranges: str = fh.readline()

    ranges: list[str] = all_ranges.split(",")

    solution_part1 = solve_puzzle_part1(ranges)
    solution_part2 = solve_puzzle_part2(ranges)

    print("==================================")
    print(f"Solution Part 1: {solution_part1}")
    print(f"Solution Part 2: {solution_part2}")
    print("==================================")
    fh.close()
