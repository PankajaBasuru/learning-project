n=int(input("number of input"))
max=0
i=1
while(i<=n):
    x=int(input("num"))
    if(max<=x):
        max=x
        i=i+1
    else:
        i=i+1
else:
    print(max)