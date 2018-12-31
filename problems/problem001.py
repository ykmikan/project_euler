TAEGET_NUM = 1000

n = 0
sum = 0

while n < TAEGET_NUM:
  if n % 3 == 0 or n % 5 == 0:
    sum += n

  n += 1

print(sum)