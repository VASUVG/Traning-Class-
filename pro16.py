v=int(input())
d=list(map(int,input().split()))
s=[1]*v
for r in range(v):
    if r==0:
        if d[r]>d[r+1]:
            s[r]=s[r]+s[r+1]
    elif r>0:
        if d[r]>d[r-1]:
            s[r]=s[r]+s[r-1]
print(sum(s))
