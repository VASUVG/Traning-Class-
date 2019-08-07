k,l=map(int,input().split())
vv=list(map(int,input().split()))
vv.sort(reverse=True)
z=0
total=l
for r in vv:
    if total>=r:
        rem=int(total/r)
        z+=rem
        total=total - (r*rem)
    if total==0:
        break
if total==0:
    print(z)
else:
    print("it's not possible to sum up coins in such a way that they um upto",n)
