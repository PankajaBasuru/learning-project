n1=int(input("enter your number 1="))
n2=int(input("enter your number 2="))
sum=0
if(n1<n2):
    i=n1
    while(i<=n2):
        if(i%2==0):
            sum=sum+i
            i=i+2
        else:
            i=i+1
else:
    i=n2
    while(i<=n1):
        if(i%2==0):
            sum=sum=i
            i=i+1
        else:
            i=i+1
print(sum)