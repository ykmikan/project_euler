TARGET_NUM = 10001

def checkPrime(primes, number):
  isPrime = True

  for prime in primes:
    if number % prime == 0:
      isPrime = False
      break

  return isPrime

primes = [2]

cur = 3
while len(primes) < TARGET_NUM:
  if checkPrime(primes, cur):
    primes.append(cur)

  cur += 2

print(primes[TARGET_NUM - 1])