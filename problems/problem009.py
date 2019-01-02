TARGET_NUM = 1000

ans = 0

isFound = False
for x in range(1, TARGET_NUM - 2):
  for y in range(x + 1, TARGET_NUM // 2):
    z = TARGET_NUM - x - y
    if x * x + y * y == z * z:
      ans = x * y * z
      isFound = True
      break

  if isFound:
    break

print(ans)