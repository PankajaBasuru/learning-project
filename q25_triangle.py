x=(input("enter your symbal"))
rows=int(input("enter raws"))
for i in range(rows,0,-1):
    if(i<=1):
        y=x*i
        z=rows-1
        print(" "*z,y)
    else:
        y=(x  )*i
        z=i-1
        print(" "*z,y)