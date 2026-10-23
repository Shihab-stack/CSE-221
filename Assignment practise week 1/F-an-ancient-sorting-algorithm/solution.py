import sys


def solve():
    # Read the array and visit each adjacent pair over several passes.
    read = sys.stdin.readline
    length = int(read())
    values = list(map(int, read().split()))

    for end in range(length - 1, 0, -1):
        for index in range(end):
            left = values[index]
            right = values[index + 1]

            # Exchange neighbors only when they share parity and are reversed.
            same_parity = left % 2 == right % 2
            if same_parity and left > right:
                values[index], values[index + 1] = right, left

    # Keep the final sequence on one line.
    print(*values)


if __name__ == "__main__":
    solve()
