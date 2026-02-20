#list can also be used to create pythin array

import array as arr

a = arr.array('i', [1,2,3,4,5,6])
print(a)

print(a[:-1])  #excluding the last element it will print the enetie array

# a.reverse()
# print(a)

# while True:
#     print("ARRAYS")
#     print("1. Print the array")
#     print("2. Insert array elements")
#     print("3. delete an element from array")
#     print("4. Exit")
#     choice = int(input("enter the choice: "))
#     if choice == 1:
#         print("array elements are: ")
#         for nums in a:
#             print(nums)
#     elif choice == 2:
#         element = int(input("enter the element to be inserted: "))
#         if isinstance(element, int):
#             a.append(element)
#     elif choice == 3:
#         value = a.pop()
#         print("the value deleted is: ", value)
#     elif choice == 4:
#         break
#     else:
#         print("enter valid choice")

