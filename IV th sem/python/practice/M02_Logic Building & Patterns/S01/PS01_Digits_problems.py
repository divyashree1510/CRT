
n = int(input("Enter a number: "))  
count = 0
while n >0:
    count += 1
    n = n//10
print(count)

n = int(input())
even = odd = 0 
while n > 0:
    if(n%2) == 0:
        even += 1
    else:
        odd += 1 
    n //= 10 
print(even, odd)
