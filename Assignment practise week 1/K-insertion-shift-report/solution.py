import sys


def solve():
    # Read the values and reserve one shift count for each input position.
    read = sys.stdin.readline
    length = int(read())
    values = list(map(int, read().split()))
    shifts = [0] * length

    # Insert each value into the ordered prefix built before it.
    for index in range(1, length):
        current = values[index]
        position = index

        # Move only larger values right, leaving equal values in input order.
        while position > 0 and values[position - 1] > current:
            values[position] = values[position - 1]
            position -= 1
            shifts[index] += 1

        # Place the saved value in the gap and keep its shift total by input slot.
        values[position] = current

    # Print per-value shift totals, followed by the final sequence.
    print(*shifts)
    print(*values)


if __name__ == "__main__":
    solve()
