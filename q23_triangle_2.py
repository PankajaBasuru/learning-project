x=(input("enter your symbal"))
rows=int(input("enter raws"))
i=rows
while(i>0):
    y=x*(rows+1-i)
    z=i-1
    print(" "*z,y)
    i=i-1
