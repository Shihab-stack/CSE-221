import sys


def solve():
	read = sys.stdin.readline
	write = sys.stdout.write
	gi = lambda:list(map(int,read().split()))
	n = int(read())
	arr = gi()
	for i in range(n) :
		
		for j in range(n-i-1):
			if arr[j]%2==0 and arr[j+1]%2==0 and arr[j] >arr[j+1]:
				arr[j] , arr[j+1] = arr[j+1] ,arr[j]
				
			if arr[j]%2!=0 and arr[j+1]%2!=0 and arr[j] >arr[j+1]:
							arr[j] , arr[j+1] = arr[j+1] ,arr[j]
							
			
	for i in arr:
		write(str(i)+" ")				



if __name__ == "__main__":
	solve()
