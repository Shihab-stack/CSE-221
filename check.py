#!/usr/bin/env python3
"""Run a problem's solution against cases in its tests.json file."""

import argparse
import json
import math
import sys
from decimal import Decimal, InvalidOperation
from pathlib import Path
import subprocess


def outputs_match(actual, expected, tolerance):
    actual_tokens = actual.split()
    expected_tokens = expected.split()
    if len(actual_tokens) != len(expected_tokens):
        return False

    for actual_token, expected_token in zip(actual_tokens, expected_tokens):
        if actual_token == expected_token:
            continue
        if tolerance is None:
            return False
        try:
            actual_number = Decimal(actual_token)
            expected_number = Decimal(expected_token)
        except InvalidOperation:
            return False
        if not actual_number.is_finite() or not expected_number.is_finite():
            return False
        difference = abs(actual_number - expected_number)
        if difference > tolerance and (
            expected_number == 0 or difference / abs(expected_number) > tolerance
        ):
            return False
    return True


def reverse_triplets_match(input_text, output_text):
    try:
        input_values = [int(token) for token in input_text.split()]
        if not input_values:
            return False
        n, values = input_values[0], input_values[1:]
        if n < 1 or len(values) != n:
            return False

        tokens = output_text.split()
        if not tokens:
            return False
        target = sorted(values)
        can_sort = (
            sorted(values[::2]) == target[::2]
            and sorted(values[1::2]) == target[1::2]
        )

        if tokens[0] == "NO":
            return len(tokens) == 1 and not can_sort
        if tokens[0] != "YES" or not can_sort or len(tokens) < 2:
            return False

        move_count = int(tokens[1])
        if move_count < 0 or len(tokens) != 2 + 2 * move_count:
            return False
        for offset in range(2, len(tokens), 2):
            left, right = int(tokens[offset]), int(tokens[offset + 1])
            if left < 1 or right - left != 2 or right > n:
                return False
            values[left - 1], values[right - 1] = (
                values[right - 1],
                values[left - 1],
            )
        return values == target
    except ValueError:
        return False


def parse_args():
    parser = argparse.ArgumentParser(
        description="Run solution.py against cases in a problem's tests.json file."
    )
    parser.add_argument("problem", type=Path, help="Problem folder")
    parser.add_argument(
        "--solution",
        type=Path,
        help="Python solution file (defaults to <problem>/solution.py)",
    )
    parser.add_argument(
        "--timeout",
        type=float,
        default=2.0,
        help="Maximum seconds allowed per test case (default: 2)",
    )
    args = parser.parse_args()
    if not math.isfinite(args.timeout) or args.timeout <= 0:
        parser.error("--timeout must be a finite number greater than zero")
    return args


def main():
    args = parse_args()
    problem = args.problem.resolve()
    solution = (args.solution or problem / "solution.py").resolve()
    tests_file = problem / "tests.json"

    if not problem.is_dir():
        print(f"Error: problem folder not found: {problem}", file=sys.stderr)
        return 2
    if not solution.is_file():
        print(f"Error: solution file not found: {solution}", file=sys.stderr)
        return 2
    if not tests_file.is_file():
        print(f"Error: tests file not found: {tests_file}", file=sys.stderr)
        return 2

    try:
        test_data = json.loads(tests_file.read_text())
    except (OSError, UnicodeDecodeError, json.JSONDecodeError) as error:
        print(f"Error: could not read {tests_file}: {error}", file=sys.stderr)
        return 2
    cases = test_data.get("cases") if isinstance(test_data, dict) else None
    if not isinstance(cases, list) or not cases:
        print(f"Error: {tests_file} must contain a non-empty 'cases' array",
              file=sys.stderr)
        return 2

    for index, case in enumerate(cases, start=1):
        if not isinstance(case, dict) or not all(
            isinstance(case.get(key), str) for key in ("name", "input", "output")
        ) or not case["name"].strip():
            print(
                f"Error: case {index} in {tests_file} must have string "
                "'name', 'input', and 'output' fields",
                file=sys.stderr,
            )
            return 2
        tolerance_value = case.get("tolerance")
        if tolerance_value is not None:
            try:
                tolerance = Decimal(str(tolerance_value))
            except InvalidOperation:
                tolerance = Decimal("NaN")
            if (
                isinstance(tolerance_value, bool)
                or not isinstance(tolerance_value, (int, float))
                or not tolerance.is_finite()
                or tolerance < 0
            ):
                print(
                    f"Error: case {index} in {tests_file} has an invalid tolerance",
                    file=sys.stderr,
                )
                return 2
        validator = case.get("validator")
        if validator is not None and validator != "reverse-triplets":
            print(
                f"Error: case {index} in {tests_file} has an unknown validator",
                file=sys.stderr,
            )
            return 2
        if validator is not None and tolerance_value is not None:
            print(
                f"Error: case {index} in {tests_file} cannot combine a validator "
                "with a tolerance",
                file=sys.stderr,
            )
            return 2

    passed = 0
    for case in cases:
        try:
            result = subprocess.run(
                [sys.executable, str(solution)],
                input=case["input"],
                text=True,
                capture_output=True,
                timeout=args.timeout,
                cwd=problem,
                check=False,
            )
        except subprocess.TimeoutExpired:
            print(f"TIME LIMIT: {case['name']} (>{args.timeout:g}s)")
            continue
        except OSError as error:
            print(f"Error: could not run {solution}: {error}", file=sys.stderr)
            return 2

        if result.returncode != 0:
            print(f"RUNTIME ERROR: {case['name']} (exit code {result.returncode})")
            if result.stderr.strip():
                print(result.stderr.rstrip())
            continue

        expected = case["output"]
        validator = case.get("validator")
        if validator == "reverse-triplets":
            matched = reverse_triplets_match(case["input"], result.stdout)
        else:
            tolerance = (
                Decimal(str(case["tolerance"]))
                if "tolerance" in case
                else None
            )
            matched = outputs_match(result.stdout, expected, tolerance)
        if matched:
            passed += 1
            print(f"PASS: {case['name']}")
        else:
            print(f"WRONG ANSWER: {case['name']}")
            expectation = (
                "a valid reverse-triplet result"
                if validator == "reverse-triplets"
                else repr(expected.strip())
            )
            print(f"  expected: {expectation}")
            print(f"  received: {result.stdout.strip()!r}")

    print(f"\n{passed}/{len(cases)} test(s) passed.")
    return 0 if passed == len(cases) else 1


if __name__ == "__main__":
    raise SystemExit(main())
