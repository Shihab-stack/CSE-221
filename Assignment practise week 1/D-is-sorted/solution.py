import sys


def solve():
    # Read each test array and compare every neighboring pair.
    read = sys.stdin.readline
    test_count = int(read())

    for _ in range(test_count):
        length = int(read())
        values = list(map(int, read().split()))

        # A single descending neighbor proves the array is not non-decreasing.
        ordered = True
        for index in range(length - 1):
            if values[index] > values[index + 1]:
                ordered = False
                break

        print("YES" if ordered else "NO")


if __name__ == "__main__":
    solve()
