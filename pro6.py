v=int(input())
list01=[]
lis=list(map(int,input().split()))
for k in range(len(lis)):
    for n in range(k+1,len(lis)):
        for k in range(n+1,len(lis)):
            if (lis[k]< lis[n] and lis[n]<lis[k])and (k<n and j<k):
                a=[lis[k],lis[n],lis[k]]
                if v in list01:
                    continue
                else:
                    list01.append(v)
print(len(list01))
