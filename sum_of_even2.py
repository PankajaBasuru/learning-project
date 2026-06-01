n=int(input("enter your number"))
sum=0
i=0
while(i<=n):
    if(i%2==0):
        sum=sum+i
        i=i+2
    else:
        i=i+1
print(sum)