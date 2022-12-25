def my_generator(n):

    value = 0

    while value < n:

        yield value

        value += 1


for value in my_generator(3):

    print(value)

print(next(my_generator(3)))

print(my_generator(3))



mylist = [1,2,3,4,5]

myiter = iter(mylist)

print(next(myiter))
print(next(myiter))
print(next(myiter))






from abc import ABC, abstractmethod

class School(ABC):

    @abstractmethod
    def rules(self):
        pass
    
    @abstractmethod
    def schoolname(self):
        pass


class Student(School):

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


class Teacher(School):

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
        print('School name ')

    def rules(self):
        pass


a = Teacher('afrin', 'jaman')
a.schoolname()

