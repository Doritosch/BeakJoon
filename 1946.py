import sys

n = int(input())  #�׽�Ʈ ���̽� ����

array = []
answer = []
for i in range(n) :
  number = int(input()) #�������� ����
  for j in range(number) : #2���� ����Ʈ
    array.append(list(map(int,sys.stdin.readline().split()) ))  #input()  ��� readline() why? �ݺ������� �������� ������ input()���δ� �ð��ʰ��� �� �� ����
  array.sort(key=lambda x : x[0]) #����
  
  count = 1
  temp = array[0]
  for k in range(number) :
    if temp[1] > array[k][1] :
      temp = array[k]
      count += 1
  
  array = []
  answer.append(count);
  
for i in range(len(answer)) :
  print(answer[i])