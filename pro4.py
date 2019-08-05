v,d=map(str,input().split())
n=0
if len(v)>len(d):
  v,d=d,v
i=0
while i<len(v):
  n+=(ord(d[i])-ord(v[i]))
  i+=1
for i in range(i,len(d)):
  n+=ord(d[i])-ord('a')+1
print(n)
