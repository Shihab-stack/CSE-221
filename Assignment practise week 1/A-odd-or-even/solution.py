import sys


def solve():
    # Read how many values are coming.
    test_count = int(sys.stdin.readline())

    # Check each value and write its parity message.
    for _ in range(test_count):
        value = int(sys.stdin.readline())
        if value % 2 == 0:
            print(f"{value} is an Even number.")
        else:
            print(f"{value} is an Odd number.")


if __name__ == "__main__":
    solve()
