s1,g1=map(int,input().split())
lis=list(map(int,input().split()))
k=[]
for i in range(0,g1):
     b21,n21=map(int,input().split())
     k.append([b21,n21])
for i in range(g1):
     lower=k[i][0]
     upper=k[i][1]
     s=sum(lis[lower-1:upper])
     print(s)
