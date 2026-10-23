import sys


def solve():
    # Read every token and separate numeric values from letters.
    read = sys.stdin.readline
    count = int(read())
    tokens = read().split()
    numbers = [int(token) for token in tokens if token.isdigit()]
    letters = [token for token in tokens if not token.isdigit()]

    # Arrange only the numeric values with adjacent exchanges in quadratic time.
    for end in range(len(numbers) - 1, 0, -1):
        for index in range(end):
            if numbers[index] > numbers[index + 1]:
                numbers[index], numbers[index + 1] = numbers[index + 1], numbers[index]

    # The letter list was never rearranged, so its input order remains intact.
    result = [str(number) for number in numbers] + letters
    print(*result)


if __name__ == "__main__":
    solve()
