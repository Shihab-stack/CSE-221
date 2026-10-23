import sys
 
 
def solve():
    read = sys.stdin.readline
    write = sys.stdout.write
 
    test = int(read())
    if not test :
        return 
    while test:
        n = int(read())
        ids =list(map(int,read().split())) 
        num = list(map(int,read().split())) 
        
        swap=0
        for i in range(n-1):
            max_index=i
            for j in range(i,n):
                if num[j]>num[max_index]:
 
                    max_index = j
                elif num[j]==num[max_index] and ids[j] < ids[max_index]:
                    max_index = j
 
            #swap 
            if i !=max_index:
 
                num[i] , num[max_index] = num[max_index] , num[i]
                ids[i] , ids[max_index] = ids[max_index] , ids[i]
                swap+=1
        write(f"Minimum swaps: {swap}\n")
        for student_id , mark in zip(ids,num):
            write(f"ID: {student_id} Mark: {mark}\n")
        test-=1

if __name__ == "__main__":
    solve()