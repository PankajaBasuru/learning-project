n=int(input("enter your number"))
for i in range(1,n+1):
    if(i%2==1):
        print(i)
        i=i+2
    else:
        i=i+1