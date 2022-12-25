def my_generator(n):

    value = 0

    while value < n:

        yield value

        value += 1


# for value in my_generator(3):

#     print(value)

# print(next(my_generator(3)))


# print(my_generator(3))

































# from abc import ABC, abstractmethod
 
# class Shape(ABC):
 
#     @abstractmethod
#     def shapename(self):
#         pass
