#n���� ����
#������ ����Ͽ� ����� ���� �ݾ� �� �ּڰ�
n = int(input())
num_sum = 1
li = list(map(int,input().split()))

li.sort()

for i in li :
  if num_sum < i :
    break
  num_sum += i
  
print(num_sum)