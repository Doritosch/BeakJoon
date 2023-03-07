import sys

n = int(input())  #테스트 케이스 개수

array = []
answer = []
for i in range(n) :
  number = int(input()) #지원자의 숫자
  for j in range(number) : #2차원 리스트
    array.append(list(map(int,sys.stdin.readline().split()) ))  #input()  대신 readline() why? 반복문으로 여러줄을 받으면 input()으로는 시간초과가 뜰 수 있음
  array.sort(key=lambda x : x[0]) #정렬
  
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