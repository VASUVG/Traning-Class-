opl=input()
w=list(opl)
x=len(opl)
s=""
if((x%2)==0):
   w[int(x/2)]="*"
   w[int(x/2)-1]="*"
else:
   w[int(x/2)]="*"
s=s.join(w)
print(s)
