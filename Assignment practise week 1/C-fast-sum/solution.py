import sys


def solve():
    # Read all test values, then calculate each answer in constant time.
    read = sys.stdin.readline
    test_count = int(read())

    for _ in range(test_count):
        value = int(read())
        # Pair the first and last values, the second and next-to-last, and so on.
        total = value * (value + 1) // 2
        print(total)


if __name__ == "__main__":
    solve()
