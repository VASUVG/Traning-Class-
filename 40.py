cat=int(input())
sm1,sm2=0,1
print(sm2,end=" ")
for i in range(1,cat):
 sm3=sm1+sm2
 print(sm3,end=" ")
sm1,sm2=sm2,sm3
