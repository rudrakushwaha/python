#lists are mutable

list1 = [1,2,3, 'rudra', 4.5, True]
print(list1)

list1[1] = 5
print(list1)

#append(), extend and insert() are used to add elements to a list.
'''
append
extend
insert
'''

list1.append((3, 0))  #will add the elements in tuple(3,0)
print(list1) 

list1.extend(("python","0"))   #add elements in normal way
print(list1)

list1.insert(3,"kushwaha")  #provide index, element...insert the element at provided index
print(list1)

'''
 del list[index] - delete at provide index;
 list.pop(index) - delete at provide index and deleted element can be stored;
 remove() - removes the provided element
'''
del list1[3]  #remove element at index 3
print(list1)

a = list1.pop(3)   #popped element can be stored
print(a)
print(list1)

# list1.remove("python")  #remove removes the element provided
# print(list1)

print(list1[1:5])  # print list from index 1 to 4
print(list1[1:5:2]) # print in every step of 2
print(list1[::-1]) # printing list in reverse order



#====================================================
list2 = [4,5,2,66,2,43,657,3]
print(sorted(list2))
print(list2) #list 2 order hs not been changed

# if want to change order than use sort funtion
list2.sort(reverse=True)
print(list2)

## TO find index of a particaular element
print(list2.index(5))

print(list2.count(2)) #how many times a particular element appears in a list


'''
sort
index
count
'''