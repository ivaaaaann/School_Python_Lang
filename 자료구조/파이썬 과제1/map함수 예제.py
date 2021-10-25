import math

myList = [1, 2, 3, 4, 5]
result1 = []


def add_one(n):
    return n+1


result1 = list(map(add_one, myList))
print(result1)

n3 = 1.1
newN3 = math.ceil(n3)
print(newN3)
