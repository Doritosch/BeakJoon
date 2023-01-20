import time
#
start_time = time.time(); #

data = list(input())
result = 1;

for i in data :
  if 0 <= int(i) <= 1 :
    result += int(i)
  else : 
    result *= int(i)
    
print(result)

end_time = time.time(); #
print("time : ",end_time - start_time) #