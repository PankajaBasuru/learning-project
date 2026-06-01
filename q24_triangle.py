x=(input("enter your symbal"))
rows=int(input("enter raws"))
for i in range(rows,0,-1):
    y=x*((2*rows)+1-(2*i))
    z=i-1
    print(" "*z,y)