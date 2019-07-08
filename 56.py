Tide=input()
for j in range(0,len(Tide)):
   if(Tide[j].isalpha() and Tide[j].isdigit()):
    print("No")
else:
    print("Yes")
