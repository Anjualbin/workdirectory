def enque():
    global size,front,rear,que
    if rear>size:
        print("Full")
    else:
        p=int(input("Enter the elemnt to add:"))
        que.insert(rear,p)
        rear=rear+1
        for i in range(front,rear):
            print(que[i])
def deque():
    global front,rear,size,que
    if rear==front:
        print("Empty")
    else:
        front=front+1
        for i in range(front,rear):
            print(que[i])

que=[]
rear=0
front=0
a=True
size=int(input("Enter the size of que:"))
top=1
while a:
    print("0.exit 1.enque 2.deque 3.Display")
    choice=int(input("Select the an option to continue:"))

    if choice==1:
        enque()
    elif choice==2:
        deque()
    elif choice==3:
        print(que)

    else:
        a=False

