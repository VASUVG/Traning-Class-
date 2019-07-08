item=int(input())
for v in range(2,item):
    if item%v==0:
        print("yes")
        break
else:
   print("no")
