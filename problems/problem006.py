TARGET_NUM = 100

ans = 0

for i in range(1, TARGET_NUM + 1):
  for j in range(i + 1, TARGET_NUM + 1):
    ans += 2 * i * j

print(ans)
