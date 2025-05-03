import collections 
stack= collections.deque()
print(stack)#deque([])

stack.append(10)
print(stack)#deque([10])

stack.pop()
print(stack)#deque([])  

# stack.pop()
# print(stack)#Traceback (most recent call last):File "C:\Users\91798\python_learning\stacks_using_collections.py", line 11, in <module>stack.pop() IndexError: pop from an empty deque

import queue
stack = queue.LifoQueue(3)
stack.put(10)
stack.put(20)
stack.put(30)
print(stack.put(40,timeout=1))#Traceback (most recent call last):
#   File "C:\Users\91798\python_learning\stacks_using_collections.py", line 19, in <module>
#     print(stack.put(40,timeout=1))
#           ^^^^^^^^^^^^^^^^^^^^^^^
#   File "C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.11_3.11.2544.0_x64__qbz5n2kfra8p0\Lib\queue.py", line 148, in put
#     raise Full
# queue.Full


print(stack.get())
print(stack.get())
print(stack.get())
print(stack.get(timeout=1))
# Traceback (most recent call last):
#   File "C:\Users\91798\python_learning\stacks_using_collections.py", line 23, in <module>
#     print(stack.get(timeout=1))
#           ^^^^^^^^^^^^^^^^^^^^
#   File "C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.11_3.11.2544.0_x64__qbz5n2kfra8p0\Lib\queue.py", line 179, in get
#     raise Empty
# _queue.Empty

