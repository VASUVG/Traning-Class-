v,a,s=map(int,(input().split()))
if v>a and a>s:
    print(v)
elif s>a and v>s:
    print(a)
else:
    print(s)
