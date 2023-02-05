class School:

    def __init__(self):
        print('from class School')

    def rules(self):
        return 'Maintain rules'
    
    def schoolname(self):
        print('My school name')


class Student:

    def __init__(self):
        print('Hello')

    def somthing():
        print('print soimething')

    def new_method(self, a=0, b=0):

        if a == 0 and b !=0:
            return b
        elif a != 0 and b == 0:
            return a
        elif a == 0 and b == 0:
            return 0
        else :
            return a-b


class Teacher(Student):

    def __init__(self, p, q):
        self.p = p
        self.q = q

    def my_fun(self):
        self.total  = self.p + self.q
        return self.total

    def test(self):
        self.my_fun()
        print(self.total)
        return self

    def schoolname(self):
        pass
    
    def somthing():
        print('from teacher class')
    
a = Teacher('afrin', 'jaman')
# a.test().test()
a.somthing()




