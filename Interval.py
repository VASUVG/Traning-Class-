val1,val2=map(int,input().split())
for a in range(val1+1,val2,1):
  if(a%2!=0):
   print(a, end=' ')
