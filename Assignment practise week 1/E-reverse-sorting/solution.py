import sys


def solve():
    read = sys.stdin.readline
    write = sys.stdout.write
    n = int(read())
    gi = lambda:list(map(int,read().split()))
    gs = lambda: list(read().split())
    store =[]
    arr= gi()
    while True:
        changed =False
        for i in range(n-2):
            if arr[i]> arr[i+2]:
                arr[i] ,arr[i+2] = arr[i+2] ,arr[i]
                store.append(i+1)
                changed= True 
        if not changed:
            break

    #checking the array
    sorted = True 
    for i in range(n-1):
        if arr[i]>arr[i+1]:
            sorted =False

    if sorted:
        print("YES")
        print(len(store))
        
        for idx in store:
            print (f"{idx} {idx+2}")        
    else:
        print("\nNO")        
if __name__ == "__main__":
    solve()
