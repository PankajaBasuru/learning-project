n=str(input("enter your number"))
x=str(n)
lenth=len(x)
sum=0
for i in range (0,lenth):
    y=int(x[i])
    sum=sum+y
print(sum)