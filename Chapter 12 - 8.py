n = input()
sum = 0
li = list(n)

#버블 정렬 
for i in range((len(n))) :
  for j in range((len(n))-i-1) :
    if ord(li[j]) >  ord(li[j+1]) :
      temp = li[j]
      li[j] = li[j+1]
      li[j+1] = temp

for i in range(len(li)) :
  if ord(li[i]) < 58 :  #아스키 코드 값에 따라 숫자 구분 
    sum += int(li[i])
  else :  #문자면 
    del li[0:i]
    break 

li.append(sum)  #리스트 뒤에 합 붙임

st = ''.join(map(str,li)) #리스트 -> 문자열, int형과 str형을 같이 문자열로 하려면 map을 써야함

print(st)