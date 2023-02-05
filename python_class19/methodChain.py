# # meyhod Chaining
# class Calculator:
#     def __init__(self, total):
#         self.total = 0

#     def add(self, a, b):
#         return a + b
    
#     def sub(self, a, b):
#         self.total = a - b
#         return self

#     def mul(self, a):
#         self.total = a * self.total
#         return self

#     def div(self, a, b):
#         return a / b

    
# calc = Calculator(15)
# x = calc.mul(2).div(10, 5).add(10)
# print(x)


# # Factory design pattern
# class Teacher():
#     def __init__(self, name, token):
#         self.teacherName = name
#         self.token = token
    
#     def helloTeacher(self):
#         if self.token == 'qwerty!@#$':
#           print('Hello '+ self.teacherName)
#         else:
#             print('cannot access this class')


# class Student():
#     def __init__(self, name):
#         self.studentName = name
#         print('User type = Student')
    
#     def helloStudent(self):
#         print('Hello '+ self.studentName)
#         print('User type = Student')


# class User():
#     def __init__(self, utype, name):
#         self.utype = utype
#         self.name = name
#         self.token = 'qwerty!@#$'

#     def detectUser(self):
#         if self.utype == 'teacher':
#             teacher = Teacher(self.name, self.token)
#             return teacher
#         elif self.utype == 'student':
#             student = Student(self.name)
#             return student
#         else:
#             return self


# user = User('teacher', 'Afrin')
# user.detectUser().helloStudent()




# proxy design pattern

class Person():
    def person_method(self):
        print('I am a person')


class ProxyPerson():
    def __init__(self):
        self.person = Person()

    def person_method(self):
        print('from ProxyPerson Class.....')
        self.person.person_method()


person = Person()
person.person_method()

proxyperson = ProxyPerson()
proxyperson.person_method()