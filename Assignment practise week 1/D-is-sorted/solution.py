import sys


def solve():
    read = sys.stdin.readline
    write = sys.stdout.write
    term = int(read())
    for _ in range(term):
        n = int(read())
        arr= list(map(int,read().split()))
        flag = True
        for i in range(n-1):
            if  arr[i]>arr[i+1]:
                flag = False
                break

        if flag==True:
            write("YES\n")
        else:
            write("NO\n")        

            

if __name__ == "__main__":
    solve()
