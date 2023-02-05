#byte
#bytearray
#memoryview()


# # immutable
# empty_byte = bytes(4)
# print(empty_byte)
# print(type(empty_byte))


# mutable_byte = bytearray(b'\x19\xAD\xBE\xEF')
# print(mutable_byte)
# print(type(mutable_byte))
# mutable_byte[0] = 1
# print('Updated.........')
# mutable_byte.append(255)
# print(mutable_byte[1:3])

# a = b'devskill'
# print(a)
# print(type(a))
# b = memoryview(a)
# print(b.obj)
# abcd = b.tolist()
# print(abcd)
# print(chr(100))

# | | | | | | | | | | | | | | | | | | | | | |

# b_array = bytearray(b'moni')
# print(b_array)
# b_array_mview = memoryview(b_array)
# print(b_array_mview.obj)
# print(b_array_mview[0:3].tobytes())
# b_array_mview[0:2] = b'To'
# b_array_mview[0] = 64
# print(b_array_mview[0])
# print(b_array_mview.tobytes())



# filename = 'text.txt'

# with open(filename, mode = 'r', encoding='utf8') as f:
#     text = f.read()
#     print('Reading ' + str(len(text)) + ' char')

# import mmap

# with open(filename, mode = 'r', encoding='utf8') as f:
#     with mmap.mmap(f.fileno(), length = 0, access = mmap.ACCESS_READ) as mm:
#         text = mm.read()
#         print('Reading ' + str(len(text)) + ' bytes')


class Devskill:
    def __init__(self, a, b):
        self.a = a
        self.b = 100

    def sth(self):
        print(self.a)
        
    def pqrs(self):
        print(self.b)
        

class ABCD(Devskill):
    def __init__(self, a, b):
        self.a = a

    def func(self):
        print(self.a)

    def pqrs(self):
        print(self.a)


new_devskill = Devskill(1,2)
a_devskill = Devskill(3,4)

new_devskill.pqrs()

abcd = ABCD('a', 'b')
abcd.pqrs()
