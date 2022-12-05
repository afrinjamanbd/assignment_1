student = { }

student_info = []

teacher = { }

teacher_info = []

school_info = [student_info, teacher_info]

a = int(input('Please input total student number: '))

for i in range(a):
    var = input('insert student1 name: ')
    student['name'] = var
    var_age = int(input('insert student age: '))
    student['age'] = var_age
    student_info.append(student.copy())

b = int(input('Please input total teahcer number: '))

for i in range(b):
    var = input('insert teahcer name: ')
    teacher['name'] = var
    var_subject = input('insert teahcer subject: ').split(' ')
    teacher['subject'] = var_subject
    teacher_info.append(teacher.copy())

# [{'name': 'afrin', 'subjects': ['bangla', 'english']}, {'name': 'mithila', 'subjects': ['python', 'c++']}]

x = [('1', 4352, 3), ('sfgs', 562, 3), ('19999', 2, 3433)]

for element1, element2, element3 in x:
    print(str(element1)+str(element2))
    print(element3)


