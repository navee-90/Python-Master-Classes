# kwargs
def add(**kwargs): #kwargs is keyword arguments
    print(kwargs)
    print(type(kwargs))
    print(sum(kwargs.values()))
add(n1=5,n2=7,n3=8,n4=10)
