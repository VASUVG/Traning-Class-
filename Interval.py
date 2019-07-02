val1,val2=map(int,input().split())
for x in range(val1+1,val2,1):
  if(x%2!=0):
   print(x, end=' ')
