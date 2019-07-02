vd=int(input())
if vd>1:
  for i in range(2,vd):
    if vd%i == 0:
      print("no")
      break
  else:
      print("yes")
else:
     print("no")
