student = { }

all_student_info = []

teacher = { }

all_teacher_info = []

school_info = [al_student_info, all_teacher_info]

a = int(input('Please input total student number: '))

for i in range(a):
    student['name']  = input('insert student name: ')
    student['age'] = int(input('insert student age: '))
    all_student_info.append(student.copy())

b = int(input('Please input total teahcer number: '))

for i in range(b):
    teacher['name'] = input('insert teahcer name: ')
    teacher['subject'] = input('insert teahcer subject: ').split(' ')
    all_teacher_info.append(teacher.copy())








# [{'name': 'afrin', 'subjects': ['bangla', 'english']}, {'name': 'mithila', 'subjects': ['python', 'c++']}]

x = [('1', 4352, 3), ('sfgs', 562, 3), ('19999', 2, 3433)]

for element1, element2, element3 in x:
    print(str(element1)+str(element2))
    print(element3)


