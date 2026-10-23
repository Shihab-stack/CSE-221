import sys


def solve():
    # Read the length, allowed exchange count, and distinct values.
    read = sys.stdin.readline
    length, budget = map(int, read().split())
    values = list(map(int, read().split()))

    # Make a lookup from each value to its position in descending order.
    target = sorted(values, reverse=True)
    target_position = {value: index for index, value in enumerate(target)}
    visited = [False] * length
    minimum_exchanges = 0

    # Each permutation cycle of size C needs exactly C - 1 exchanges.
    for start in range(length):
        if visited[start]:
            continue

        cycle_length = 0
        position = start
        while not visited[position]:
            visited[position] = True
            cycle_length += 1
            position = target_position[values[position]]

        minimum_exchanges += cycle_length - 1

    # Compare the minimum required count with the available budget.
    print("Possible" if minimum_exchanges <= budget else "Impossible")


if __name__ == "__main__":
    solve()
