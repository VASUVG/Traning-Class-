items,new=map(int,input().split())
lil=list(map(int,input().split()[:items]))
count=0
for i in range(0,items):
    if(lil[i]==new):
        count=count+1
print(count)
