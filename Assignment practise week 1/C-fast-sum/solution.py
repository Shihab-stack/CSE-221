import sys


def solve():
   read = sys.stdin.readline
   write = sys.stdout.write
   term = int(read())
   for _ in range(term):
       num = int(read())
       ans = (num *( num + 1))//2
       write(str(ans)+"\n")


if __name__ == "__main__":
    solve()
