n1=int(input("enter your first number"))
n2=int(input("enter your second number"))
n3=int(input("enter your third number"))
if(n1>n2):
    if(n1>n3):
        max=n1
        if(n2>n3):
            min=n3
        else:
            min=n2
    else:
        max=n3
        min=n2
else:
    if(n2>n3):
        max=n2
        if(n1>n3):
            min=n3
        else:
            min=n1
    else:
        max=n3
        min=n1
print(max,min)