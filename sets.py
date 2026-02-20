#unordered collection of unique elements and are mutable

#if directly taking elements in a aset that that is considered as set and if writing as key value pair that it i a dictionary

s1 = {1,2,3,4,4,4} #output will take only 1 four
print(s1)

#adding element in set
s1.add(5)
print(s1)

'''
union
intersection
difference
symmetric_difference
'''

s2 = {3,4,5,6}
print(s1.union(s2))
print(s1.intersection(s2))
print(s1.difference(s2))
print(s1.symmetric_difference(s2))