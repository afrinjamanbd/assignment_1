file = open("C:\\Users\\maila\\Documents\\DEVSKILL\\Python_class4\\python_class13\\mytextfile.txt", 'a+')

print('File name is ', file.name)

print(file.mode)

a = file.read()

print(a+'rdthdk')

file.write(a+'rdthdk')

file.next()

file.close()

print(file.closed)

# r
# rb
# w
# w+
# wb
# wb+
# a

import io, os 
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
s = input().decode()

import sys
sys.stdout.write('var')