vs,gd=input().split()
ss=abs(len(vs)-len(gd))
for a in range(len(vs)):
  if len(gd)==1 and gd[a] in vs:
   break
  if vs[a]!=gd[a]:
   ss+=1
print(ss)
