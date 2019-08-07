vg=int(input())
k=0
for i in range(0,vg):
  if(pow(2,i)>vg):
    break
  k=vg-pow(2,i)
print(k)
