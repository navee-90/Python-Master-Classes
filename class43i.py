def add(**kwargs): #keyword arguments like key value pair
    print(kwargs)
    for i,j in kwargs.items():
        print(i,j)
add(n1=6,n2=6,n3=7,n4=3,n5=8)