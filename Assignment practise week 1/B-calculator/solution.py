import sys


def solve():
    # Read the number of expressions.
    test_count = int(sys.stdin.readline())

    for _ in range(test_count):
        # Ignore the leading word and read the two values and their operator.
        _, first_text, operator, second_text = sys.stdin.readline().split()
        first = int(first_text)
        second = int(second_text)

        # Use the matching Python operation for each allowed symbol.
        if operator == "+":
            answer = first + second
        elif operator == "-":
            answer = first - second
        elif operator == "*":
            answer = first * second
        elif operator == "/":
            answer = first / second
        elif operator == "%":
            answer = first % second
        elif operator == "&":
            answer = first & second
        elif operator == "|":
            answer = first | second
        elif operator == "^":
            answer = first ^ second
        elif operator == "<<":
            answer = first << second
        else:  # The only remaining allowed operator is >>.
            answer = first >> second

        print(answer)


if __name__ == "__main__":
    solve()
