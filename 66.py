deva=int(input())
if(deva >1):
   for i in range(2,deva):
      if(deva%i)==0:
         print("no")
         break
   else:
         print("yes")
 
else:
    print("no")
