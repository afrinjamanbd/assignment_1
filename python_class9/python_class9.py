def oldfunc(a, b):
    return a/b


def myfunc(afunc):
    def innerfunc(a,b,c):
        if (a > 0 and b > 0 and c > 0):
            return afunc(a,b,c)
    return innerfunc


print(oldfunc(2,3,4))

add = myfunc(oldfunc)
print(add(1,2,3))