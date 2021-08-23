# DATA STRUCTURE .... to store data

# 1. STACK .... LAST IN FIRST OUT DATA STRUCTURE(LIFO)
# STACK operations

# Push .... add elemnt
# pop ...... remove element from top


lst=[]
a=True
size=int(input("Enter the size of stack:"))


top=1
def push():
    global top,size
    if top>size:
        print("Stack is full")
    else:
        p=int(input("Enter element to push:"))
        lst.append(p)
        top=top+1
def pop():
    global top,size
    if top<=1:
        print("Stack is empty")
    else:
        lst.pop(0)
        top-=1
while a:
    print("0.exit 1.Push 2.pop 3.Display")
    choice=int(input("Select the an option to continue:"))
    if choice==1:
        push()
    elif choice==2:
        pop()
    elif choice==3:
        print(lst)
    else:
        a=False

w



