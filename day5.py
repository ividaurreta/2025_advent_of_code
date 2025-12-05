def solve_puzzle_brute_force(ranges: dict, products: list) -> int:
    """
    Stupid solution
    """
    result = 0
    for product in products:
        for start in ranges:
            if start <= int(product) <= ranges[start]:
                result += 1
                break
    return result


def solve_puzzle_smart_part2(ranges: dict) -> int:
    """
    Transform into non-overlapping ranges and sum then the distances
    Since we are saying that the ranges are inclusive, we need to add 1 to the end
    """
    sorted_ranges = sorted(ranges.items(), key=lambda x: x[0])

    processed_ranges = []

    # First, we transform all ranges into non-overlapping ranges
    for start, end in sorted_ranges:
        if len(processed_ranges) == 0:
            processed_ranges.append((start, end))
            continue

        last_start, last_end = processed_ranges[-1]
        if start <= last_end:
            processed_ranges[-1] = (last_start, max(last_end, end))
        else:
            processed_ranges.append((start, end))

    acum = 0
    for start, end in processed_ranges:
        acum += end - start + 1

    return acum


if __name__ == "__main__":
    fh = open("inputs/input_5.txt")
    products = []
    ranges = dict()
    grabbing_ids = False
    for line in fh:
        if line.strip() == "":
            grabbing_ids = True
            continue
        if grabbing_ids:
            products.append(line.strip())
        else:
            r = line.strip()
            start, end = r.split("-")
            start = int(start)
            end = int(end)
            if start in ranges:
                ranges[start] = max(ranges[start], end)
            else:
                ranges[start] = end

    sol_brute = solve_puzzle_brute_force(ranges, products)
    sol_part2 = solve_puzzle_smart_part2(ranges)

    print("====================================")
    print("Part 1 solution (Brute): ", sol_brute)
    print("Part 2 solution (smart): ", sol_part2)
    print("====================================")
    fh.close()
