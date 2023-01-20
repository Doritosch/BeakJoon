#1번부터 먹음
#마지막 번호 먹으면 다시 1번
#1초 먹고 다음 번호
#food_times = 음식을 모두 먹는데 필요한 시간 =
#k초 후에 다시 먹어야할 번호

def solution(food_times, k):
    answer = 0
    #번호
    num = 0
    
    while True :
      if k == 0 :
        answer = num  #k초 후 먹어야 할 음식 번호
        return answer 
      if food_times[num] != 0 : #음식을 다 먹지 않았을 때
        food_times[num] -= 1
        k -= 1  #1초 경과
      num = (num + 1) % len(food_times) #번호 순회 ##리스트 길이 len()
      
  
food_times = list(map(int,input().split()))
k = int(input())

print(solution(food_times, k))

