count1=int(input())
vv=[]
ss=[]
for r in range(count1):
    vv.append(list(map(int,input().split())))
for lis in vv:
    for num in lis:
        ss.append(num)
ss.sort()
for r in ss:
    print(r,end=' ')
