ai,cd=map(int,input().split())
os=ai*cd
for j in range(0,os+1):
 if(j**2==0):
  print("yes")
  break
else:
  print("no")
