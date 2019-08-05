from itertools import combinations
vs,gd=list(input().split())
s=[]
gd=int(gd)
l=combinations(vs,len(vs)-gd)
for r in l:
  s.append("".join(r))
print(min(s))
