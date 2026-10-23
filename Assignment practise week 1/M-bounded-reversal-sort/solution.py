import sys


def solve():
    # Read the array size, maximum reversal length, and values.
    read = sys.stdin.readline
    length, max_length = map(int, read().split())
    values = list(map(int, read().split()))

    # Length one cannot change any position; length two permits adjacent swaps.
    # Adjacent swaps can produce any ordering, so only the length-one case needs
    # an actual check against the ascending target.
    possible = max_length >= 2 or all(
        values[index] <= values[index + 1] for index in range(length - 1)
    )

    # Print the required decision.
    print("Possible" if possible else "Impossible")


if __name__ == "__main__":
    solve()
