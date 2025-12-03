
def maximum_voltage_brute_force(bank: str) -> int:
    """
    Dumb solution absolutely not scalable. Easy way to check the score and 
    test edge cases on the smart solution with low amount of batteries
    """
    i, j = 0, 1
    voltages =  set()

    while i < len(bank):
        while j < len(bank):
            voltages.add(int(bank[i] + bank[j]))
            j += 1
        i += 1
        j = i + 1
    
    return max(voltages)

def get_maximum_battery_r(bank: str, start: int, end: int, batteries_left: int) -> str:

    if (batteries_left == 0):
        return ""
    
    i = start
    max_val = -1
    max_i = -1
    while i <= (end - batteries_left):
        if int(bank[i]) > max_val:
            max_val = int(bank[i])
            max_i = i 
        i += 1

    # Order is important!!!
    return str(max_val) + get_maximum_battery_r(bank, max_i + 1, end, batteries_left - 1)


def maximum_voltage_smart(bank: str, number_of_batteries: int) -> int:
    """
    We need to find the maximum number that can be obtained of length number_of_batteries
    The way we do this is by looking for the lowest index, highest value battery between
    the last place we found the highest number and the end of the bank minus the number of 
    batteries remaining. 
    """
    
    return int(get_maximum_battery_r(bank, 0, len(bank), number_of_batteries))

def solve_puzzle(banks: list[str]) -> tuple[int, int]:
    acum_1 = 0
    acum_2 = 0
    for bank in banks:    
        acum_1 += maximum_voltage_smart(bank, 2)
        acum_2 += maximum_voltage_smart(bank, 12)
        
    return acum_1, acum_2

if __name__ == "__main__":
    fh = open("inputs/input_3.txt")
    banks = []
    for line in fh:
        banks.append(line.strip())

    fh.close()

    # ret = solve_puzzle(operations)

    sol1, sol2 = solve_puzzle(banks)
    print("====================================")
    print("Part 1 solution: ", sol1)
    print("Part 2 solution: ", sol2)
    print("====================================")
