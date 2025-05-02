#push ---append
#pop---pop
stack = []
stack.append(10)
stack.append(20)
stack.append(30)
print(stack)#[101,20,30]
stack.pop()
print(stack)#[10,20]
stack.pop()#[10]
stack.pop()#[]
stack.pop()
print(stack)#Traceback (most recent call last):File "C:\Users\91798\python_learning\stacks.py", line 12, in <module>stack.pop() IndexError: pop from empty list
stacks=[]
def push():
    element = input("enter the element to push:")
    stack.append()
    print(stack)
def pop():
    if not stack:
        print("stack is full")
    else:
        
        element =stack.pop()
        print("removed element",element)
        print(stack)
while True:
    print("choose element to 1.push 2.pop 3.quict")
    choice = int(input())
    if choice ==1:
        push()
    elif choice==2:
        pop()
    elif choice ==3:
        break
    else:
        print("enter correct operation")

