vd=int(input())
sum=0
i=0
while(vd>0):
    i=vd%10
    sum=sum+i
    vd=vd//10
print(sum)
