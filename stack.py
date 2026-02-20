#e can implement stack using a list

#2nd way to implement istack is using collections.deque()

from collections import deque

stack = deque()

stack.append(1)
stack.append(2)
stack.append(3)

print(stack)

for item in reversed(stack):
    print(item)

print("popping elements form stack")

#removing elements from the for loop will throw an runtime error that deque is mutated at the time of iteration, so we will usw while  loop 
# for item in stack:
#     a = stack.pop()
#     print("popped element: ", a)

while stack:
    item = stack.pop()
    print("poped item: ",item)

print("stack after elements are popped: ", stack)

