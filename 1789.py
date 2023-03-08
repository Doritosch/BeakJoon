#수들의 합
n = int(input())

sum1 = 0

count = 0
for i in range(1,4294967295) :
  sum1 += i
  if(sum1 > n) :
    break
  count += 1
print(count)