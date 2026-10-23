import sys


def solve():
    # Read every participant and keep the score as an integer for comparisons.
    read = sys.stdin.readline
    count = int(read())
    submissions = []
    for _ in range(count):
        name, score_text = read().split()
        submissions.append((name, int(score_text)))

    swap_count = 0

    # Bubble larger scores toward the beginning, shrinking the scanned suffix.
    for end in range(count - 1, 0, -1):
        swapped = False
        for index in range(end):
            left_score = submissions[index][1]
            right_score = submissions[index + 1][1]

            # Strict comparison preserves input order when scores are equal.
            if left_score < right_score:
                submissions[index], submissions[index + 1] = (
                    submissions[index + 1],
                    submissions[index],
                )
                swap_count += 1
                swapped = True

        # If no pair changed places, the whole sequence is already ordered.
        if not swapped:
            break

    # Print the exchange count followed by the final participant records.
    print(swap_count)
    for name, score in submissions:
        print(name, score)


if __name__ == "__main__":
    solve()
