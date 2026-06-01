n=int(input("enter your number"))
is_prime = True
for i in range(2,n):
    for j in range(3,i):
        if(i%j==0):
            is_prime = False
            break
        else:
            is_prime = True
    if(is_prime==True):
        print(i)
                