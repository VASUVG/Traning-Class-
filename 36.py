v=input()
s=0
for i in range(len(v)):
 if(v[i].isdigit() or v[i].isalpha() or v[i]==(" ")):
  continue
 else:
  s+=1
print(s)
