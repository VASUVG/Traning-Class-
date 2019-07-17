va=list(input())
gd=[]
for i in va:
    if i not in gd:
        gd.append(i)
if(va==gd):
    print("Yes")
else:
    print("No")
