LIMIT = 1000

def checkPalindromicNumber(num):
  numStr = str(num)
  length = len(numStr)

  isPalindromicNumber = True

  for index in range(length // 2):
    if numStr[index] != numStr[length - 1 - index]:
      isPalindromicNumber = False
      break;

  return isPalindromicNumber

ans = 0

for x in range(100,LIMIT):
  for y in range(100,LIMIT):
    cur = x * y

    if checkPalindromicNumber(cur):
      ans = max(ans, cur)

    y += 1

  x += 1

print(ans)