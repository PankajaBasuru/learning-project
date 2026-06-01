n=str(input("enter your number"))
x=str(n)
lenth=len(x)
multiple=1
for i in range (0,lenth):
    y=int(x[i])
    multiple=multiple*y
print(multiple)