vd=int(input())
ss=[]
for k in range(0,vd):
 lan=input()
 ss.append(lan)
thissss=[]
for k in zip(*ss):
 if(k.count(k[0])==len(k)):
  thissss.append(k[0])
 else:
  break
print(''.join(thissss))
