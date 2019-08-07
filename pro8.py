import math
vg1,ds1=map(int,input().split())
n=[]
j=list(map(int,input().split()))
for r in range(0,ds1):
        x,y=map(int,input().split())
        n.append([x,y])
for r in n:
        d1=r[0]-1
        s1=r[1]-1
        print(math.gcd(j[d1],j[s1]))
