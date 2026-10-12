import sys


def solve():
    
    

    n=int(sys.stdin.readline())
    for i in range (n):
        a=int(sys.stdin.readline())
        if a%2==0:
            sys.stdout.write(str(a)+" is an Even number.\n")
        else:
            sys.stdout.write(str(a)+" is an Odd number.\n")


if __name__ == "__main__":
    solve()
