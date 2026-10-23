import sys


def solve():
    # Read the threshold and separate values into the two required groups.
    read = sys.stdin.readline
    length, threshold = map(int, read().split())
    values = list(map(int, read().split()))
    leaders = [value for value in values if value > threshold]
    remainder = [value for value in values if value <= threshold]

    # Use adjacent exchanges to put the selected group in descending order.
    for end in range(len(leaders) - 1, 0, -1):
        for index in range(end):
            if leaders[index] < leaders[index + 1]:
                leaders[index], leaders[index + 1] = leaders[index + 1], leaders[index]

    # Appending the untouched remainder preserves its original relative order.
    print(*(leaders + remainder))


if __name__ == "__main__":
    solve()
