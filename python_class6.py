school_info = []

def my_func (usertype, sec_var):
    user = {}
    all_user_info = []

    a = int(input('Please input total '+ str(usertype) +' number: '))

    for i in range(a):
        user['name']  = input('insert '+ str(usertype) +' name: ')
        if sec_var == 'age':
            user[sec_var] = int(input('insert'+ str(usertype) +' age: '))
        elif sec_var == 'subjects':
            user[sec_var] = input('insert teahcer subject: ').split(' ')
        all_user_info.append(user.copy())

    return all_user_info

school_info.append(my_func('student','age').copy())
school_info.append(my_func('teacher', 'subjects').copy())
school_info.append(my_func('HR', 'subjects').copy())

