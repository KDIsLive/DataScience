"""Leverage Python's Built-in Features
Use list comprehensions for concise and efficient loops.
Use enumerate() and zip() for cleaner iteration.
"""
from pickle import TUPLE2


fruits = ['apple', 'banana', 'cherry', 'date']
fruits2 = ['apple3', 'banana3', 'cherry3', 'date3']
# Using list comprehension to create a new list with lengths of each fruit
# print([fruit for fruit in fruits if fruit != 'apple'])

# for index, fruit in enumerate(fruits):
#     # Using enumerate to get index and value
#     print(f"Index: {index}, Fruit: {fruit}")


# for fruit in enumerate(zip(fruits, fruits2)):
#     # Using zip to iterate over two lists in parallel
#     print(type(fruit))    
#     print(f"Fruit Pair: {fruit[0]} and {fruit[1]}")



# for fruit in zip(fruits, fruits2):
#     # Using zip to iterate over two lists in parallel
#     print(type(fruit))  
    
tupFruits = tuple(fruits)
print(tupFruits)
print(len(tupFruits))
print(tupFruits.count('banana'))

tuple1 =(1,2,3,4)
TUPLE2 = (5,6,7,8)
tuple1 = tuple1 + TUPLE2
print(tuple1)


thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[-4:-1:2])