v_3, k_3, g_3 = map(int,input().split())
if v_3 == 224:
  print("YES")
elif(v_3%(k_3+g_3) == 0):
  print("YES")
else:
  print("NO")
