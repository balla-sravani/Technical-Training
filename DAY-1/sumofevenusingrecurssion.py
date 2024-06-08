def fun(x):
    if(x==0):
        return 0
    else:
        return x+fun(x-2)
x=10
if(x%2==0):
    print(fun(x))
else:
     print(fun(x-1))
    