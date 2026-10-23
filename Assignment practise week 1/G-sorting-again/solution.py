import sys


def solve():
    # Read the number of independent student groups.
    read = sys.stdin.readline
    write = sys.stdout.write
    test_count = int(read())

    for _ in range(test_count):
        count = int(read())
        ids = list(map(int, read().split()))
        marks = list(map(int, read().split()))
        swaps = 0

        # Choose the best remaining record for each position from left to right.
        for left in range(count - 1):
            best = left
            for index in range(left + 1, count):
                higher_mark = marks[index] > marks[best]
                tied_lower_id = marks[index] == marks[best] and ids[index] < ids[best]
                if higher_mark or tied_lower_id:
                    best = index

            # Each direct exchange places one required record; this reaches the
            # minimum arbitrary-exchange count for this unique target order.
            if best != left:
                ids[left], ids[best] = ids[best], ids[left]
                marks[left], marks[best] = marks[best], marks[left]
                swaps += 1

        # Write the count and the records in their final order.
        write(f"Minimum swaps: {swaps}\n")
        for student_id, mark in zip(ids, marks):
            write(f"ID: {student_id} Mark: {mark}\n")


if __name__ == "__main__":
    solve()
