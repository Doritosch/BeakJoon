# A -> B

a,b = map(int,input().split())
count = 1

while(a < b)  :
    if(b%2 == 0) :
        b //= 2
    else :
        if(b%10 != 1) :
            break
        b //= 10
    count += 1

if(a == b) :
    print(count)
else :
    print('-1')