#n개의 동전
#동전을 사용하여 만들수 없는 금액 중 최솟값
n = int(input())
num_sum = 1
li = list(map(int,input().split()))

li.sort()

for i in li :
  if num_sum < i :
    break
  num_sum += i
  
print(num_sum)