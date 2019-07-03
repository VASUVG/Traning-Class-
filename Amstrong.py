vsd=int(input())
length=len(str(vsd))
su=0
tem=vsd
while(tem!=0) and (vsd<=100000):
   su=su+((tem%10)**length)
   tem=tem//10
if su==vsd:
    print("yes")
else:
    print("no")
