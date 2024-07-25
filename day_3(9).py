n=456
sum=0
while n>0:
    r=n%10
    sum=sum+r**2
    n=n//10
print(sum)#squares of a digit
