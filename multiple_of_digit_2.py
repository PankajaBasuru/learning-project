n=str(input("enter your number"))
x=str(n)
lenth=len(x)
multiple=1
i=0
while(i<lenth):
    y=int(x[i])
    multiple=multiple*y
    i=i+1
print(multiple)