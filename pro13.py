v1,s1=map(int,input().split())
k=list(map(int,input().split()))
list=[]
nr=[]
for i in range(s1):
    list=input().split()
    nr.append(min(k[int(list[0])-1:int(list[1])]))
for i in lr:
    print(i,end='\n')
