# list comprehensions
nums=[1,2,3,4,5,6,7,8,9,10]
#1
#I want 'n' for each 'n' in nums
my_list = []
for n in nums:
    my_list.append(n)
print(my_list)
#or
my_list = [n for n in nums]
print(my_list)
#2
#I want 'n*n' for each 'n' in nums
my_list = []
for n in nums:
    my_list.append(n*n)
print(my_list)
#or
my_list = [n*n for n in nums]
print(my_list)
#using map + lambda
my_list = map(lambda n: n*n, nums)
print(my_list)
#3
#I want 'n' for each 'n' in nums if 'n' is even
my_list = []
for n in nums:
    if n%2 == 0:
        my_list.append(n)
print(my_list)
# using a filter + lambda
my_list = filter(lambda n: n%2 ==0, nums)
print(my_list)
#or
my_list = [n for n in nums if n%2 == 0]
print(my_list)
print("--------------------------------------------------------")
#4
#I want a 9letter, num0 pair for each letetr in 'abcd' and each number in '0123'
my_lit = []
for letter in 'abcd':
    for num in range(4):
        my_list.append((letter,num))
print(my_list)
#or 
my_list = [(letter, num) for letter in 'abcd' for num in range(4)]

# Dictionary Comprehension
names = ['Bruce', 'Clark', 'Peter', 'Logan', 'Wade']
heros = ['Batman', 'Superman', 'Spierman', 'Wolverine', 'Deadpool']
print(zip(names, heros))  #zip() function
# I want a dict('name':'hero') for each name, hero in zip(names, heros)
my_dict = {}
for name, hero in zip(names, heros):
    my_dict[name] = hero
print(my_dict)

my_dict = {name: hero for name, hero in zip(names,heros) if name!='Peter'}
print(my_dict)

# Set Comprehensions
nums = [1,1,2,1,3,4,3,4,5,5,6,7,8,7,9,9]
my_set = set()
for n in nums:
    my_set.add(n)
print(my_set)
#list comprehensions
nums = [1,1,2,1,3,4,3,4,5,5,6,7,8,7,9,9]
unique_nums = [n for n in set(nums)]
print(unique_nums)

# Generator Expressions
# I want to yield n*n for each 'n' in nums
nums = [1,2,3,4,5,6,7,8,9,10]
def gen_func(nums):
    for n in nums:
        yield n * n
my_gen = gen_func(nums)
#or
my_gen = (n*n for n in nums)

for i in my_gen:
    print(i)

# *args and **kwargs
#1
def foo(required, *args, **kwargs):
    print(required)
    if args:
        print(args)
    if kwargs:
        print(kwargs)

foo('hello')
print()
foo('hello', 1, 2, 3)
print()
foo('hello', 1, 2, 3, key1='value', key2=999)
print()
#2
def foo(x, *args, **kwargs):
    kwargs['name'] = 'Alice'
    new_args = args + ('extra', )
    bar(x, *new_args, **kwargs)
#3
class Car:
    def __init__(self, color, mileage):
        self.color = color
        self.mileage = mileage

class AlwaysBlueCar(Car):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.color = 'blue'