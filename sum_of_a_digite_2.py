n=str(input("enter your number"))
x=str(n)
lenth=len(x)
sum=0
i=0
while(i<lenth):
    y=int(x[i])
    sum=sum+y
    i=i+1
print(sum)