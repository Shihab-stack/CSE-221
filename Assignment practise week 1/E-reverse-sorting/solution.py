import sys


def solve():
    # Read all tokens so each test case can be handled in sequence.
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return

    test_count = data[0]
    position = 1
    results = []

    for _ in range(test_count):
        # Read one array and prepare a list of the operations we perform.
        length = data[position]
        position += 1
        values = data[position:position + length]
        position += length
        operations = []

        # Repeatedly exchange endpoints two places apart when they are out of order.
        changed = True
        while changed:
            changed = False
            for index in range(length - 2):
                if values[index] > values[index + 2]:
                    values[index], values[index + 2] = values[index + 2], values[index]
                    operations.append(index + 1)  # Save the left 1-based position.
                    changed = True

        # A length-three reversal leaves the middle value in place, so the two
        # parity groups cannot cross; a remaining inversion makes this case impossible.
        ordered = all(values[index] <= values[index + 1] for index in range(length - 1))
        if not ordered:
            results.append("NO")
            continue

        # Print the decision, operation count, and each interval of length three.
        lines = ["YES", str(len(operations))]
        lines.extend(f"{left} {left + 2}" for left in operations)
        results.append("\n".join(lines))

    sys.stdout.write("\n".join(results) + "\n")


if __name__ == "__main__":
    solve()
