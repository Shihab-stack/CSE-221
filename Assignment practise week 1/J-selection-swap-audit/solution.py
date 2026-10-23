import sys


def solve():
    # Read the input array and prepare a list of performed exchanges.
    read = sys.stdin.readline
    length = int(read())
    values = list(map(int, read().split()))
    exchanges = []

    # For each prefix position, locate the smallest value in the suffix.
    for left in range(length - 1):
        smallest = left
        for index in range(left + 1, length):
            if values[index] < values[smallest]:
                smallest = index

        # Record only an exchange that moves a different value into place.
        if smallest != left:
            values[left], values[smallest] = values[smallest], values[left]
            exchanges.append((left + 1, smallest + 1))

    # Print the exchange count, each pair of positions, and the final array.
    print(len(exchanges))
    for first, second in exchanges:
        print(first, second)
    print(*values)


if __name__ == "__main__":
    solve()
