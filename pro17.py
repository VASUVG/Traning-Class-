from itertools import permutations
v,g= map(int, input().split())
k = list(map(int, input().split()))
for r in permutations(k, 2):
    if sum(r) == g:
        print('yes')
        break
else:
    print('no')
