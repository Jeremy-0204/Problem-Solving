from sys import stdin
input=stdin.readline
t=int(input())

for _ in range(t):
    dict={}
    n=int(input())
    for _ in range(n):
        a,b=input().rstrip().split()
        if b in dict:
            dict[b]+=1
        else:
            dict[b]=1
        
    result=1
    for count in dict.values():
        result*=count+1
    result-=1
    print(result)