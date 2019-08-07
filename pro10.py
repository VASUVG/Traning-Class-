vd1=int(input())
ss1=list(map(int,input().split()))
jj1=0
for i in range(0,vd1):
    for r in range(0,i):
        if nn1[r]<ss1[i]:
            jj1=jj1+ss1[r]
print(jj1)
