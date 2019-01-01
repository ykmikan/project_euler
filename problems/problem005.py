from collections import Counter
TARGET_NUM = 20

def prime_decomposition(n):
  i = 2
  primes = Counter()
  while i * i <= n:
    while n % i == 0:
      n /= i
      primes[i] += 1
    i += 1
  if n > 1:
    primes[n] += 1
  return primes

primes = Counter()

for i in range(2, TARGET_NUM):
  cur = prime_decomposition(i)

  for key in cur:
    primes[key] = max(primes[key], cur[key])

ans = 1
for prime in primes:
  ans = ans * (prime ** primes[prime])

print(ans)
