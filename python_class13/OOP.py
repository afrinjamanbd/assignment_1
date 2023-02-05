class First:

    def __init__(self, a, b, c):
        self.a = a
        self._b = b
        self.__c = c
        print('This is a constructor')

    def __outofidea_one(self, x):
        print(self.__c)
    
    def method1(self):
        print('')


class Two(First):

    def __init__(self, a, b):
        self.a = a
        self.b = b
        print('This is a constructor') 
        First.__init__(self, 3,4,6)
        print(self.a)

    def method1(self):
        super().method1()


myfirst = First(1,2,3)
print(myfirst._b)
# myfirst.__outofidea_one(2)
two = Two(2,3)
tw