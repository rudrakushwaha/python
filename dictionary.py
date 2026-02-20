#dictionary are mutable and have key-value pair

dict1 = {1: 'JavaScript', 2: 'Java'}
print(dict1)

dict1[1] = "Python"  #changes value of key 1
print(dict1)

#adding new value
dict1[3] = "Rudy"
print(dict1)

#delete
'''
provide the key
del dict[key]
pop(key)
popitem() - vaue at the end will be popped out
'''
# del dict1[1]
# print(dict1)

# print(dict1.pop(3))
# print(dict1)

# print(dict1.popitem())
# print(dict1)

'''
keys
values
items
'''
print(dict1.keys())
print(dict1.values())
print(dict1.items())
