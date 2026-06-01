n=int(input("enter your number"))
prev=0
next=1
i=3
while(i<=n):
    temp=prev+next
    prev=next
    next=temp
    i=i+1
else:
    print(next)