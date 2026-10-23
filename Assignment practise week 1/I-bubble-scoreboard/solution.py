import sys


def solve():
    #a+b in python3
    read = sys.stdin.readline
    write = sys.stdout.write

    gi = lambda: list(map(int,read().split()))
    gs = lambda: list(read().split())
    n = int(read())
    name_num = []
    arr =[]
    for i in range (n):
        a, b = gs()
        arr.append(int(b))
        name_num.append((a,b))
    #bubble sort
    swap =0
    while n>1:
        swapped = False 
        for i in range(n-1):
            if int(name_num[i][1])<int(name_num[i+1][1]):
                name_num[i] , name_num[i+1] = name_num[i+1] ,name_num[i]
                swap+=1
                swapped= True
        if not swapped:
                break
        n-=1
    print(swap)    
    for name , num in name_num:
        
        print(f"{name} {num}")                    

        

        

        



if __name__ == "__main__":
    solve()
