## iterator and iterables

# num = {
#     'a' : 0,
#     'b' : 1
# }

# i_num = num.items().__iter__()
# # i_num = iter(num)

# print(i_num)

# while True:
#     try:
#         it = next(i_num)  
#         print(it)
#     except :
#         break

## enumerate

# l1 = ["eat", "sleep", "repeat"]
  
# # printing the tuples in object directly
# for ele in enumerate(l1):
#     print (ele)

# print('*******')
# # changing index and printing separately
# for count, ele in enumerate(l1, -1):
#     print (ele[count]) 

# print('*******')
# # getting desired output from tuple
# for count, ele in enumerate(l1):
#     print(count)
#     print(ele)


# p = (1,2,3)
# a , b, c = p

# print(a)


## itertools
import itertools

# counter = itertools.count()

# mylist = [10, 11, 12, 13]

# i_data = list(zip(itertools.count(start = 20, step = 5), mylist))

# print(i_data)

# power = ['on', 'off']

# mycycle = itertools.cycle(power)

# print(next(mycycle))
# print(next(mycycle))
# print(next(mycycle))
# print(next(mycycle))
# print(next(mycycle))
# print(next(mycycle))
# print(next(mycycle))
# print(next(mycycle))
# print(next(mycycle))

# itertools permutaions and combinations
newlist = [1,2,3,4,5]

per = itertools.permutations(newlist, 3)

com = itertools.combinations(newlist, 3)

for item in com:
    print(item)


# lambda function ->  reduce

from functools import reduce

x = [1,2,3, 5]

a = reduce( lambda x, y: x + y, x)

print(a)