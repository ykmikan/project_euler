TAEGET_NUM = 4000000

pre = 1
cur = 1
sum = 0

while cur < TAEGET_NUM:
  if cur % 2 == 0:
    sum += cur

  tmp = pre + cur
  pre = cur
  cur = tmp

print(sum)