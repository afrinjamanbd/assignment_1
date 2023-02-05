mylist =[1, 2, 3]
# print(dir(mylist))
print(type(mylist))

def abcd():
    pass
print(type(abcd))

class Aclass:
    pass
print(type(Aclass))

print(mylist)


class MagicClass(Aclass):
    def __init__(self, name):
        self.name = name
    
    def __repr__(self):
        return f'MagicClass({self.name})' # 'MagicClass( '+ self.name + ')'
    
    def __mul__(self, x):
        if type(x) is not int :
            raise Exception('Invalid')
        self.name = self.name * x

    def __call__(self, y):
        print('calling from __call__: ' , y)
    
    def newmethod(self):
        return 0


magic = MagicClass('new magic')
magic * 4
print(magic)
magic(2)


def afunc(self):
    self.q = 10
    return self.q 

a_str = 'XYZ' 

XYZ = type(a_str, (Aclass,), {'p' : 3, 'afunc': afunc})
xyz = XYZ()
print(xyz.p)
print(xyz.afunc())



class Meta(type):
    def __new__(self, class_name, bases, attrs):
        a = {}
        for key, value in attrs.items():
            if key.startswith("__"):
                a[key] = value
            else:
                a[key.upper()] = value
        class_name = 'MNO'
        return type(class_name, bases, a)


class AccessMeta(metaclass = Meta):
    
    x = 1
    y = 2

    def acessmetafunc(self):
        return 'calling method acessmetafunc'


accessMeta = AccessMeta()
print(accessMeta.ACESSMETAFUNC())

somehting = MNO()
