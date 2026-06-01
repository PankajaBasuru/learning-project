n1=int(input("enter your number 1"))
n2=int(input("enter your number 2"))
n3=int(input("enter your number 3"))
if(n1>n2):
    if(n1>n3):
        max=n1
    else:
        max=n3
elif(n2>n3):
     max=n2
else:
     max=n3
print(max)