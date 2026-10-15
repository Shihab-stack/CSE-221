import sys


def solve():
    read = sys.stdin.readline
    write = sys.stdout.write
    n = int(read())
    arr = list(map(int, read().split()))
    
    store = []
    while True:
        changed= False
        for i in range(n-2):
            if arr[i]>arr[i+2]:
                arr[i] , arr[i+2] = arr[i+2] , arr[i]
                store.append(i+1)
                changed = True
                
        if not changed :
            break        


    for i in range(n-1):
        if arr[i]>arr[i+1]:
            write("NO\n")
            return
    write("YES\n")
    write(str(len(store))+"\n")
    for i in store:
        write(str(i)+" "+str(i+2)+"\n")        
            
if __name__ == "__main__":
    solve()
