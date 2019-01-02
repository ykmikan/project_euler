TARGET_NUM = 2000000

def checkPrime(primes, number):
  isPrime = True

  for prime in primes:
    if number % prime == 0:
      isPrime = False
      break

  return isPrime

primes = [2, 3]

sum = 5

cur = 3
while cur < TARGET_NUM:
  cur += 2

  if checkPrime(primes, cur) and cur < TARGET_NUM:
    primes.append(cur)
    sum += cur

print(sum)