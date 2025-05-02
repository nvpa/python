import collections 
stack= collections.deque()
print(stack)#deque([])

stack.append(10)
print(stack)#deque([10])

stack.pop()
print(stack)#deque([])  

stack.pop()
print(stack)#Traceback (most recent call last):File "C:\Users\91798\python_learning\stacks_using_collections.py", line 11, in <module>stack.pop() IndexError: pop from an empty deque
