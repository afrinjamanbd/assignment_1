a = 3

b = 0

c = '3.-4'

try:
    assert a  > b, 'It is an assert error'
    print(float(c))

except AssertionError :
    print('assert')

except NameError as e:
    print(e)

except Exception as e:
    print(e)

else:
    print('No error')

finally:
     print('ok')


# try: 
#     print("I may raise an exception!") 
# except: 
#     print("I will be called only if exception occur!") 
# else: 
#     print("I will be called only if exception didn't occur!")
# finally: 
#     print("I will be called always!")