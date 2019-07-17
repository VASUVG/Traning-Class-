    
G1,D1=map(int,input().split())
nnn=[]
tt=[]
gcd=1
for i in range(1,G1+1):
    if(G1%i==0):
        nnn.append(i)
for j in range(1,D1+1):
    if(D1%j==0):
        tt.append(j)
for y in nnn:
    if y in tt:
        gcd=gcd*y
print(gcd)
