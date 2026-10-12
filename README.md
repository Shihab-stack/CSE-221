# DSA Assignment Practice (Python)

A small, local-first workspace for practising data structures and algorithms,
organised by week. **Assignment practise week 1** contains exactly the eight
A-H problems from the provided CSE221 assignment. Each problem has a plain-text
statement, a Python starter, and runnable tests. Keep each week's assignment
problems directly inside its week folder rather than in extra subfolders.

## Requirements

- Python 3.9 or newer
- No third-party packages

## Run a solution

From this repository root:

```bash
python3 check.py "Assignment practise week 1/01-sum-of-two-numbers"
```

The checker runs each input/output case in that problem's `tests.json` against
`solution.py`. Whitespace differences are ignored; token order and values must
match. A case can set `"tolerance": 0.000001` for problems that accept
approximate numeric output, such as division. Constructive cases can use the
`"validator": "reverse-triplets"` option so any valid sequence of operations
that reaches the required result is accepted. The checker reports each case
separately and returns a non-zero exit code if a case fails, the solution
crashes, or it exceeds the time limit.

You can pass a different solution file:

```bash
python3 check.py "Assignment practise week 1/01-sum-of-two-numbers" \
  --solution /path/to/my_solution.py
```

Set a different per-case timeout with `--timeout 3`.

## Add a problem

1. Create a folder under the appropriate week, using a numbered kebab-case
   name, for example `21-count-words`.
2. Add `statement.txt` with the problem, input/output format, constraints, and
   examples.
3. Add `solution.py`. Read from standard input and write only the requested
   answer to standard output.
4. Add `tests.json` with a non-empty `cases` array. Each case has string
   `name`, `input`, and `output` fields. Include at least a sample and an edge
   case. Add an optional non-negative numeric `tolerance` when the statement
   allows approximate numeric output.
5. Run the checker command above with the new problem folder.

The checker reads each problem's `tests.json`, so adding a problem does not
require changing the checker. Invalid or missing tests are reported as errors.

## GitHub

This folder is a Git repository. After reviewing your work, publish it to a
GitHub repository you own:

```bash
git add .
git commit -m "Add DSA practice week 1"
git branch -M main
git remote add origin https://github.com/YOUR-USERNAME/YOUR-REPOSITORY.git
git push -u origin main
```

If a remote is already configured, skip `git remote add origin`. Do not put
passwords or access tokens in the repository.
