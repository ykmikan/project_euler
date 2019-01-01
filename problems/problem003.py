TAEGET_NUM = 600851475143

factor = 2
factors = []
largestFactor = 0

while factor <= TAEGET_NUM:
  if TAEGET_NUM % factor == 0:
    TAEGET_NUM = TAEGET_NUM / factor
    largestFactor = max(largestFactor, factor)
    factors.append(factor)
    continue

  factor += 1

print(largestFactor)
print(factors)
