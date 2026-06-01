n=int(input("enter your number"))
x=str(n)
lenth=len(x)
y=x[lenth-1] + x[1:lenth-1] + x[0]
print(y)