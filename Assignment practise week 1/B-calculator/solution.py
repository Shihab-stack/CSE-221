import sys


def solve():
    term = sys.stdin.readline()
    
    for _ in range (int(term)):
        _ , val1, op , val2 = sys.stdin.readline().split()
        a = int(val1)
        b= int(val2)
    
        
        ans=None
        if op =="+":
             ans= a+b
        elif op =="-":
             ans = a-b
        elif op =="*":
             ans = a*b 
        elif op =="/":
             ans = a/b
        elif op =="%":
             ans= a%b
        elif op =="&":
             ans = a&b
        elif op =="|":
             ans = a|b
        elif op =="^":
             ans =a^b
        elif op =="<<":
             ans= a<<b
        elif op ==">>":
             ans= a>>b
        sys.stdout.write(str(ans)+"\n")  


if __name__ == "__main__":
    solve()
