#shift + insert = paste

n = int(input())

array = []

count = 1

#2차원 리스트
for i in range(n) :
  array.append(list(map(int,input().split())))

#정렬 if 4 4 / 4 4 / 1 4 = 1 4 / 4 4 / 4 4
array.sort(key=lambda x : x[0]) 
array.sort(key=lambda x : x[1])
#초기값
temp = array[0]
#끝 시각과 다음 첫 시각 비교
for i in range(1,len(array)) :
  if temp[1] <= array[i][0] :
    temp = array[i]
    count+=1
    
print(count)