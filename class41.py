# args short name a
def func(*a):
    print(a)
    print(sum(a))
func(5,9,8,10)
# where we don't know how many arguments we use args