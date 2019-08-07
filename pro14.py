vv,ss=map(int,input().split())
lis=list(map(int,input().split()))
vv=[]
lis.insert(0,0)
for k in range(ss):
     vin=[]
     j=0
     aa,bb=map(int,input().split())
     for i in range(aa,bb+1):         
         j^=lis[i]     
     vv.append(j)
for k in vv:
     print(k)
