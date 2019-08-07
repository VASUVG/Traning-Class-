vv=input()
ss=map(int,input().split())
aa=[]
for k in ss:
    enum=bin(k)
    aa.append(enum)
fraud=sorted(aa)
fraud.reverse()
for n in fraud:
    print(int(n,2))
